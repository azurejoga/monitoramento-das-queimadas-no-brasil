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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9972c67-4309-3e5f-a432-59b0fdff4600 | -13.76062 | -53.42379 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d27884b2-e10a-374a-aae4-e62c6268ba05 | -14.06693 | -53.61559 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b7c84548-c431-3dc7-a123-9415cb2dbf57 | -14.43998 | -51.85939 | 2026-08-14 00:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 9faa6e16-53a9-37a6-8d1b-0900a17c4ed3 | -20.03542 | -48.01385 | 2026-08-14 00:09:00 | TERRA_M-M | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 84616e3b-5dbe-3128-b642-878574bfdc57 | -15.05579 | -52.69269 | 2026-08-14 00:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c10cdf78-cbcc-3152-befc-35637624f552 | -14.08353 | -53.66584 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 9b389d5b-9e49-35b7-ac23-6f46e178bfff | -11.46117 | -44.5568 | 2026-08-14 00:09:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 63a82b43-d5b5-3998-8193-d00d4fb2a892 | -12.02236 | -47.82422 | 2026-08-14 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 089acafc-9a37-3ecf-9303-eeb9aca3ced5 | -11.33136 | -46.23376 | 2026-08-14 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 83b65bda-3aff-397c-ae51-d30cb64f3ccb | -11.88593 | -45.95847 | 2026-08-14 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fd57014c-2799-3a8f-b4de-e100f3400e14 | -14.09245 | -53.65166 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6db0d8af-9e12-3762-8b52-30b2cb2626bc | -15.09444 | -48.65415 | 2026-08-14 00:09:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6bc99490-cd73-31ac-a6ba-74ca795623b4 | -14.94689 | -46.62082 | 2026-08-14 00:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e773176d-cbf9-3aec-a139-103cd656ad04 | -15.13649 | -41.55831 | 2026-08-14 00:09:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 118.5 |
| f0c59672-d40f-3b81-b1a1-ec43ff804a04 | -20.89968 | -50.5045 | 2026-08-14 00:09:00 | TERRA_M-M | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d602bfdf-1ddb-352d-9a26-490ebe5ba5f5 | -13.25328 | -54.20044 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 82ae66ba-5ce3-36cf-afc6-1f94b0f46fff | -13.65237 | -46.25938 | 2026-08-14 00:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 15d36082-c38c-3f64-a7b2-6510ad7f493b | -12.03177 | -47.82279 | 2026-08-14 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c342064d-1009-34f9-9367-82456270cae1 | -15.1006 | -50.44394 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 1e23da17-de91-364c-b518-8778fcbe1ced | -14.44935 | -51.85804 | 2026-08-14 00:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a11377aa-be2c-30b1-a18c-875ace987137 | -11.85976 | -51.95837 | 2026-08-14 00:09:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| be409299-2bba-3df8-99cc-3c040349a0bd | -15.16681 | -50.05165 | 2026-08-14 00:09:00 | TERRA_M-M | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b86186d8-dbae-3f47-bf72-cb1ba465307e | -14.03521 | -53.58625 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 28ffd93b-5041-364d-a778-7070dfe4dd42 | -14.04719 | -53.59766 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e6a54c9d-e84e-3c8c-878f-803e6c63d813 | -13.82449 | -53.79728 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b772ceb5-892d-3bbb-8266-0c9ce02bb154 | -14.71305 | -52.89372 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b440b177-5514-368d-ab85-44ca91251681 | -11.80446 | -51.88304 | 2026-08-14 00:09:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d591ce64-e2b5-3ba1-8007-5fc5cf9afb74 | -18.54786 | -48.17728 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67b55d89-a094-3c72-8f18-5cb340622598 | -13.27816 | -54.22517 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| d5cc4d88-89e2-388e-8699-8258b3ba1f7b | -14.71932 | -47.15001 | 2026-08-14 00:09:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 32524e38-cabf-394b-9ee5-caf14883540f | -14.72307 | -52.89256 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f9862651-e8f2-38bd-8a32-c6ba1324b9fa | -10.97885 | -50.54481 | 2026-08-14 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7c440da3-3012-3c8e-a5cb-4cdc8d35f2bc | -13.25874 | -50.37437 | 2026-08-14 00:09:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 42632130-777e-3223-9d16-747717fc5062 | -10.84515 | -50.2426 | 2026-08-14 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a7b8890d-9736-3b37-bc0a-96e9ad9daf2a | -11.47586 | -44.57213 | 2026-08-14 00:09:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| f9f75828-5490-3211-9329-2b5bdec63e9f | -17.59494 | -46.69685 | 2026-08-14 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d2a1e26b-1dfa-31ec-970c-0393e50b62e7 | -14.44785 | -45.68702 | 2026-08-14 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 14beef06-ef7a-31f5-a258-c99d8dd0b391 | -20.03672 | -48.02324 | 2026-08-14 00:09:00 | TERRA_M-M | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 10ce38f9-4a60-3107-a3cb-a48eedc6e51c | -16.916 | -54.13346 | 2026-08-14 00:09:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 24b0d7e8-eba1-3762-979f-7c264452daa3 | -14.45068 | -51.8684 | 2026-08-14 00:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d33d4c79-eb17-3a80-8f37-00cd6de42d69 | -18.54296 | -48.20663 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fec2f18a-0e32-37cd-bdae-997a55658f09 | -11.3225 | -45.21796 | 2026-08-14 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| f7641b2e-8d68-32d1-b221-03add445d418 | -14.44982 | -45.69995 | 2026-08-14 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 068872a8-9fe1-3e4c-a4f6-bc62401bf74c | -13.23835 | -54.25847 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| a0a9599d-dd6a-3cb7-8974-b9537ed27ac4 | -11.50281 | -54.60252 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 1a869460-aaa0-398a-b602-769f0f16ffca | -19.95234 | -45.54943 | 2026-08-14 00:09:00 | TERRA_M-M | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ce3d9def-d7b8-3711-8cd7-bfb9e4d9d4fc | -14.72164 | -52.8808 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 27de82ce-622b-3d00-a013-6319773e9edb | -20.11517 | -50.48299 | 2026-08-14 00:09:00 | TERRA_M-M | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 8e85c8ca-1523-37bb-8471-e9ab55d31f83 | -14.9372 | -46.62238 | 2026-08-14 00:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ac23fa5a-1ce2-3d4b-a1dc-87ba3886c813 | -13.27649 | -54.21151 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 45ee7078-f7e6-3763-a3c9-8f9234cd2b63 | -14.07128 | -53.62091 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f6ac0a58-8f86-33a5-93db-cb983806d7bf | -13.24749 | -54.24319 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| b4d7f35a-250f-3b42-ae79-7f56376bdc8d | -11.86893 | -51.95707 | 2026-08-14 00:09:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1421a107-d1b5-3520-ad81-e7feedb05fae | -11.31308 | -45.22601 | 2026-08-14 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3d5878aa-eacd-3379-8f5c-0056d39b0802 | -18.47458 | -51.74279 | 2026-08-14 00:09:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2608ac82-f8ea-3a03-963e-e82114f72e26 | -11.88389 | -45.94503 | 2026-08-14 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 64c4888f-68e7-3ecd-a7fb-057b60f00f21 | -20.02658 | -48.01527 | 2026-08-14 00:09:00 | TERRA_M-M | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7e6d4f91-b381-3ab6-add7-441ad3d83856 | -13.23359 | -54.25085 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| bf8e08a3-427b-3da9-b9a1-7f374c2235e6 | -16.90644 | -54.15045 | 2026-08-14 00:09:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1315e979-25e3-33fb-883a-2c601b82e7b3 | -18.65248 | -47.944 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bc67467f-fe3c-3b11-a30d-f885888f5ed8 | -18.09914 | -52.83623 | 2026-08-14 00:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a21b7951-d464-3dce-8dcb-5cb497d30465 | -15.05408 | -52.68685 | 2026-08-14 00:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4505d579-ac25-3c8f-b34b-6703b3ffa594 | -14.08044 | -53.64001 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 283facbd-5251-33df-8a3f-ea7b1c6955c3 | -14.44131 | -51.86971 | 2026-08-14 00:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 98c38eb0-4587-3e74-ba2b-b33e8df5dc45 | -17.56659 | -47.50473 | 2026-08-14 00:09:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c8a37ad2-ae0e-3e06-9273-13ebf9f80224 | -13.26571 | -54.21281 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 565531b0-8c63-3878-bf88-1f09594af5f0 | -16.91785 | -54.14972 | 2026-08-14 00:09:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 759c0355-22f6-3039-96df-c72d2a11fa9c | -14.9971 | -46.60586 | 2026-08-14 00:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 91ecfb48-23d9-3896-bf08-6504b26e1808 | -14.45571 | -45.69313 | 2026-08-14 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| d181bfa4-68dd-36b2-abf8-f3012c6c1dac | -11.07168 | -50.94539 | 2026-08-14 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d28407d4-7844-3352-95f4-fce15c60f23a | -15.09935 | -50.43464 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2a030807-a1e7-3faa-9683-cdf1c18a105e | -15.14487 | -41.5768 | 2026-08-14 00:09:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 91.6 |
| a0844819-842f-3619-8720-0a5c58f93b93 | -19.59218 | -46.90995 | 2026-08-14 00:09:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4d97b7ed-7fa8-39e2-97b7-2d5ca883e877 | -18.42298 | -45.20723 | 2026-08-14 00:09:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f1af8cce-6e41-32f5-9afc-3336085ad5e6 | -13.5586 | -47.6693 | 2026-08-14 00:09:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 5fb8906f-e722-35a6-b270-c2c9d6f1c10b | -15.70254 | -48.32788 | 2026-08-14 00:09:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4917d23e-a4ac-39f2-8033-cb43f34258f6 | -14.0909 | -53.63877 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 12adb90d-8151-3eb2-8c01-b9b6e15ef0f4 | -13.25113 | -50.38471 | 2026-08-14 00:09:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e159aa17-d083-3122-956d-6f0cfe4d47e9 | -13.25494 | -54.21417 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a84d3436-016f-33e4-8c0c-2d9407817e48 | -18.41105 | -45.19699 | 2026-08-14 00:09:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 907aece8-ed79-386e-85b1-e9ce89f5ceef | -14.47646 | -45.68964 | 2026-08-14 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 59771f79-f3da-3fea-aad4-9ec988a07baa | -14.44533 | -45.69489 | 2026-08-14 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| b7d46feb-f6fa-3b39-b652-c5426641ea88 | -17.00853 | -47.22343 | 2026-08-14 00:09:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 64728e4a-7ba1-353a-b580-0af5f815c5d6 | -11.59537 | -54.69737 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2c004539-624b-3864-b611-4c0cf79d6c0e | -14.3609 | -53.0911 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6837dbde-20d6-3b2e-ab9f-ef7a9395a1bd | -18.29429 | -46.08677 | 2026-08-14 00:09:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f299212a-8f21-3d2f-8bcd-8e3683e18733 | -13.2499 | -50.37565 | 2026-08-14 00:09:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d51f4bfb-763b-3208-8346-206870273598 | -10.97763 | -50.53588 | 2026-08-14 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0979b758-7a0e-3589-8735-9af9eb264be5 | -15.63489 | -48.89772 | 2026-08-14 00:09:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 59c4946a-022b-3e61-a3f3-302da7fd17a1 | -13.93044 | -53.9594 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4e118db2-71bc-3d27-8591-b4d018292c53 | -19.59073 | -46.90004 | 2026-08-14 00:09:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2bd54534-a5a4-37a6-9f62-28af1be47151 | -15.14096 | -41.5842 | 2026-08-14 00:09:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 48.2 |
| 0988e5e0-1dd2-3bb6-855d-5d438f7fac2a | -14.04561 | -53.58493 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 8a9b5a0e-a667-3104-9765-96e216e21347 | -11.44921 | -44.55881 | 2026-08-14 00:09:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 000700d8-5da8-31b2-9f39-728727490cfa | -13.24916 | -54.25715 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 75408331-d82d-3de6-8812-caf72092cde2 | -11.49372 | -54.61765 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 4965bf72-3db3-301b-8cda-5279dcb4d03d | -20.79471 | -48.98465 | 2026-08-14 00:09:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5d9e0a46-59d1-309c-9fbd-a936f251d3b1 | -16.88126 | -54.12695 | 2026-08-14 00:09:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c9dc5703-e651-39d2-81b2-40a10b3a6184 | -11.49545 | -54.6315 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| a62826ef-9481-3e3b-b786-d725001cff3b | -11.51536 | -54.61506 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |


[Clique aqui para ver as próximas entradas](README3.md)
