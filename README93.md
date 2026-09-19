# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c442e8a-1ae1-3c5a-9eee-bf315519881e | -10.90123 | -53.99036 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaf9337c-bc06-35f6-9b2e-585700ef3668 | -12.4868 | -50.0465 | 2026-09-19 04:59:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 003e2cc8-9840-3a10-bba9-59ccc3891951 | -13.61183 | -46.92868 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21df14d9-3498-322c-93c1-ffd5e55fc22a | -10.88624 | -54.06329 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ee7519e-20e6-31a1-b41a-0ae479fa5b4e | -15.6301 | -52.72437 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73727da9-3461-33ea-9d6c-a267d21078df | -14.14851 | -45.21594 | 2026-09-19 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4a845b2-a093-393f-bc83-2ff0118bc393 | -14.18125 | -47.85902 | 2026-09-19 04:59:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97c13626-cf21-35c5-9a6f-f769dc83674c | -12.69336 | -45.95101 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5732ace9-54a0-3ff6-b46d-96da8887e553 | -13.30254 | -51.64409 | 2026-09-19 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9da436c7-a5d7-384f-8502-43097f17dfb4 | -11.27155 | -54.11876 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02a4b494-ed55-37f5-82e8-4337c591c927 | -12.59938 | -50.8763 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3834ce8-2eca-3fba-b3b5-b700ff4c60e9 | -18.81955 | -48.25188 | 2026-09-19 05:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d253be4-ca1a-3446-ab66-c822d22215d4 | -22.00631 | -56.08821 | 2026-09-19 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e9477d-80ce-34ae-99b6-6ebbd63457ff | -18.02355 | -51.07359 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fdc15dd8-c857-3bb5-8c0b-79974168cec1 | -22.03425 | -49.55155 | 2026-09-19 05:01:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3850a9ec-5aac-3211-bac4-478f63f73c4f | -20.45373 | -47.5894 | 2026-09-19 05:01:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43879226-887d-31a1-93f6-dc3180737838 | -22.00963 | -56.08881 | 2026-09-19 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b327e2d1-6c95-3200-aa70-a175fa758b16 | -18.01902 | -51.07797 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d3facede-2077-334f-a25c-d54e4dfb071a | -18.01835 | -51.08286 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 97e92d5d-be6a-3a5a-9a5f-0aea62ad4600 | -18.87669 | -49.513 | 2026-09-19 05:01:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 847d86a2-d6db-344e-9082-0df6c1fd4ec7 | -18.67997 | -54.84493 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a9c98ea-6e8b-3790-ab5d-190fe8cec16a | -20.85347 | -49.0658 | 2026-09-19 05:01:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| aa3d3fcc-bbc9-3c4e-a024-fd7e25bfe46c | -20.45308 | -47.59533 | 2026-09-19 05:01:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 961e1f96-2ee5-357b-bc12-b59c55e0ee49 | -18.6794 | -54.84861 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e14a8b9-29e3-3d86-bb91-ece4560c0bfa | -18.82916 | -47.93178 | 2026-09-19 05:01:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df6526a3-5f60-312f-b6d1-52a0b36af350 | -22.02581 | -49.54597 | 2026-09-19 05:01:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c1ba96be-d7c8-3406-824f-2bf547e838c0 | -18.81087 | -48.24527 | 2026-09-19 05:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee069ec4-310a-35c0-91fb-785871da013a | -18.8244 | -47.93116 | 2026-09-19 05:01:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0a512ae5-7d43-3884-8759-032bb668fa81 | -21.0214 | -47.26197 | 2026-09-19 05:01:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcf84b66-d286-3573-b73f-ad4e87b8976d | -18.81025 | -48.2504 | 2026-09-19 05:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77b9fc8e-8efe-351c-bb24-9b8e3942ad86 | -21.02175 | -47.25869 | 2026-09-19 05:01:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfdb8053-bf92-3c2e-b21a-9a1266c058b5 | -22.0382 | -49.5567 | 2026-09-19 05:01:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6336affd-aaa5-3ecf-bb01-fca528b5ca00 | -18.8724 | -49.51239 | 2026-09-19 05:01:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d09f291-015b-366b-bfa5-ca991b6010d0 | -18.01768 | -51.08774 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 298019d0-68ac-3b90-bffa-aa690c20f349 | -18.01383 | -51.08715 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f599aeb9-b934-3f78-b13d-8d7f7845a64b | -18.02287 | -51.07854 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bdb63715-6dcc-331f-b741-777ab2bbb073 | -18.87489 | -49.511 | 2026-09-19 05:01:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dd7c9d7a-be31-31a9-bb6f-6f730dac7a79 | -18.81783 | -48.24812 | 2026-09-19 05:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d73e2644-fdde-3916-9dfe-996bccd58fe9 | -18.01518 | -51.07735 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 563b6abf-115d-30e3-9b49-cb8493e9cb7c | -22.02634 | -49.5413 | 2026-09-19 05:01:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cf64d55f-6879-3ccc-a1fa-1767ca15f90a | -18.87438 | -49.51517 | 2026-09-19 05:01:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 81973de5-aaa4-337e-b8eb-e4a1b98f1460 | -18.82854 | -47.93704 | 2026-09-19 05:01:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 975fde35-136a-3992-a01a-0e8121c8f276 | -20.85242 | -49.06874 | 2026-09-19 05:01:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| d7bc06ea-df55-3c3a-be37-0c287e86ae40 | -18.41148 | -49.16595 | 2026-09-19 05:01:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cc5f3cd7-137b-3db9-bf43-5a31fd090cf0 | -18.0197 | -51.07301 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8d834686-44cd-3f47-aa68-c5f460d99ecb | -18.01451 | -51.08226 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c74e9d8a-e1e7-3920-98bf-bfff5d218df5 | -20.84787 | -49.06816 | 2026-09-19 05:01:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 513bb521-23ee-323f-b6ff-6ef9fb79c2c3 | -18.01586 | -51.0724 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ab8e915c-eb7f-3c0d-94e2-f3ffa7e80f51 | -18.80623 | -48.24447 | 2026-09-19 05:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e164325c-cf41-3e3e-8189-10ba921d9c33 | -17.95645 | -45.12201 | 2026-09-19 05:01:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02c1a684-1439-37ca-9e4b-62d2a86ba6ec | -17.95605 | -45.12583 | 2026-09-19 05:01:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe15e780-6af7-3703-bf5e-48885ed77621 | -18.87293 | -49.50821 | 2026-09-19 05:01:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ceac7f10-a0e1-3ffb-bd73-e601e087c1fd | -18.4071 | -49.16546 | 2026-09-19 05:01:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 286a8e88-ca77-3ea4-bbed-6d2faf8147bc | -18.6833 | -54.8455 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5953143-0851-3464-8a17-a62b1971b55a | -18.80853 | -48.24659 | 2026-09-19 05:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e4ba21e-404d-3b35-b0ff-8cfebed491ec | -18.02038 | -51.06805 | 2026-09-19 05:01:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9785f330-7e67-3395-96f7-e9db1f270039 | -30.15694 | -55.02199 | 2026-09-19 05:04:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 1c0dda79-8e5b-3dc0-998a-cae43dc4fc6f | -30.15331 | -55.02136 | 2026-09-19 05:04:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| f9cf99ef-ef3c-35fa-bae1-8bec5cd13396 | -30.15757 | -55.01716 | 2026-09-19 05:04:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 5.0 |
| 76a0387b-613a-3e50-ae70-02f7e3733370 | -10.7115 | -60.7312 | 2026-09-19 05:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| fe93ed53-714a-33a7-b841-2b103d8f0935 | -1.1971 | -54.22115 | 2026-09-19 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66683625-434d-3532-a21f-d6ad0516dce3 | 1.03118 | -51.11489 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e609bca-f84f-3b2c-aa37-0b04de750af1 | 3.67985 | -61.86945 | 2026-09-19 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 671cb035-f53b-3eca-a649-868cc225b93f | 1.32756 | -60.7121 | 2026-09-19 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53370757-5f37-38aa-9d8d-839707ac3d62 | 1.31019 | -60.40165 | 2026-09-19 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e30a784-37a9-36db-9060-bb7c8e8693ad | 0.78912 | -59.19918 | 2026-09-19 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85a4ab98-728d-303a-b7c3-719b895455e1 | -1.19968 | -54.22106 | 2026-09-19 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e785fddf-6e99-3f27-8f32-710e03846018 | 4.07786 | -60.01762 | 2026-09-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e169eb0-4db9-3c6f-a57a-b559f6f608e5 | 1.31086 | -60.40588 | 2026-09-19 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5dd2d6c1-1b3f-334e-aef2-7e097c54fd41 | 1.00153 | -60.4191 | 2026-09-19 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97301e22-1d08-34ea-9e6b-03247f78e43c | 2.61935 | -60.6058 | 2026-09-19 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bddfd4b8-330f-352f-b672-5c4ab5d7ceb4 | 4.08813 | -59.8976 | 2026-09-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b50f0d5a-7e40-3c44-a307-ca4d62796f56 | 3.8002 | -61.75323 | 2026-09-19 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b63a8958-2c4d-3f1e-a5c2-0a2126b63dad | -1.19459 | -54.21622 | 2026-09-19 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b9f2859-7685-35ca-ab77-a3573a15b3d7 | -1.194 | -54.22015 | 2026-09-19 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b018e1a7-fa39-306d-a771-39b683152f30 | 0.78991 | -59.20417 | 2026-09-19 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f691e32-2d20-346d-b9e3-d661acfb57a8 | 1.25687 | -50.75334 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f070ecd1-03e0-3ac6-a1d0-65e098a8ba95 | -1.19772 | -54.21722 | 2026-09-19 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8d3bc23-9e47-3f4b-b26d-746d9193fa19 | 0.85295 | -60.23754 | 2026-09-19 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b625c16-9a5b-31cb-abe8-2e79d97b4ca5 | 1.13884 | -50.99408 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d696261b-249d-3a64-8bc2-59a7f340fd1c | 1.2607 | -50.74469 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2d97de2-587a-3776-96af-05f2caeb3476 | 1.21902 | -51.00246 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb948d9d-1f91-34f5-b51b-9cfa48810874 | 4.19642 | -60.10107 | 2026-09-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 34da358b-8cae-3436-8e68-2f10cf74d108 | 1.25531 | -50.97131 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3636e6e2-80bb-30fd-ad36-597511637bb7 | 1.22473 | -50.9953 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4965d2df-4d0c-33e9-afb1-1c6071230fae | 1.26265 | -50.74604 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 301d9b50-1b9e-3fb9-b673-4c29751e322f | 1.24958 | -50.97853 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e9da5fb-aeb0-31a8-88eb-74df7e3e81ec | 1.22001 | -51.0085 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b03ca4d-5ee4-30a1-9806-83e92640f3f2 | 0.91204 | -59.62749 | 2026-09-19 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adb337fe-8db1-3521-9f6f-33734d2d58ee | -1.20027 | -54.21712 | 2026-09-19 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4da29b6b-ed8d-38a4-8ad9-156c8cfdca3f | 1.2486 | -50.97251 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9fe817e-4e2b-30f6-8e87-614811fb9d82 | -1.19203 | -54.21633 | 2026-09-19 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 638b6f0f-7eaa-3cde-851b-0dbd7af4b3bc | 1.25488 | -50.75203 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 090159d8-afb4-3869-827f-a4e22599de04 | 1.25628 | -50.97734 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eedf846c-8e82-3801-9b49-6dfcf507554e | 1.21734 | -51.01118 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6c763c0-f135-3b61-baf0-7abc27af4765 | 1.22571 | -51.00127 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6764feea-0dbf-3f23-b30e-d27a46fa3a1c | 1.13789 | -50.98817 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fe00327-af3e-3b30-a220-d312c8be07c1 | 4.43932 | -60.46508 | 2026-09-19 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a48d3e1-bc8d-3126-9a1f-2fdd566434ce | 1.21639 | -51.00515 | 2026-09-19 05:40:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a02a9b4b-9665-3642-bdae-fc83020c7138 | 2.31659 | -60.9184 | 2026-09-19 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README94.md)
