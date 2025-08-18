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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 787d7b34-0a5c-32d7-a4a5-75a684171892 | -13.59303 | -47.75565 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c401d687-24fc-3d5d-91da-0db4413b6371 | -13.24705 | -50.79451 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5a2cb7e2-5069-3ef5-a96d-45d018817c18 | -12.50657 | -57.78169 | 2025-08-18 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d340236-6e63-35d6-bf40-d9db376a4e7d | -9.5204 | -60.53244 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7eb8b5a1-3e7d-382d-9b82-93f86e8cf988 | -12.94033 | -46.11649 | 2025-08-18 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd01b761-0e0d-3d62-9f81-3be245b99205 | -13.43728 | -57.02847 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 025d6994-00a4-3649-992a-5151d153732d | -14.62313 | -54.90007 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e66cc75c-957d-3838-b169-c31a23e31f84 | -12.53551 | -48.50014 | 2025-08-18 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b7f1bcc-a42c-3afa-a3d3-30dd9c5f4bf5 | -14.6263 | -54.90543 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f4ac8c3-6e8e-384c-8b94-ed4e3ad47381 | -13.23078 | -50.75157 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f251a8f8-f47c-3610-ba28-33c213a7df49 | -11.31581 | -55.21055 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e077cd9-09b1-32cb-80d8-903285f773e1 | -14.315 | -58.93533 | 2025-08-18 05:14:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| befe2474-74ab-3e8f-842e-842f1c5a2901 | -12.99465 | -56.84613 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b38cba9-1056-36aa-8bfd-26a9ccbdb215 | -13.22072 | -50.7901 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 98c2902e-52fd-3849-ac1a-ac2cc04cd114 | -17.09646 | -49.88289 | 2025-08-18 05:14:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6c47a6e-a2f2-383d-9355-e64cc4e5383d | -13.23221 | -50.75259 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b48d0163-bc25-3e1d-9a92-17777e202b3f | -16.7944 | -50.09293 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e37ac72-5d84-3ec7-8b97-1f0598dbfbd0 | -9.51269 | -60.53521 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b40ced88-6153-363b-a520-39c8b385bb5e | -9.50983 | -60.53064 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47551e15-6616-39a0-bd58-555da05bdebc | -12.99636 | -56.85801 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ccfef83-20eb-37a3-a680-123cfc0bbed8 | -8.61816 | -62.61214 | 2025-08-18 05:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e7c448a-cb94-3ece-85cd-6b15caa3c767 | -14.62946 | -54.91082 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0673d6f2-4f52-324e-ab9a-2a903ee93ed9 | -13.45146 | -45.89259 | 2025-08-18 05:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d76c77a-33ca-37a3-99f3-3f0e4b2b1101 | -13.44669 | -45.88799 | 2025-08-18 05:14:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27bd2159-1f2c-34b4-9b65-4a095adf5545 | -13.45984 | -55.10871 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7bf354f-2380-3676-bdc7-7e89927f55ec | -13.46049 | -55.10418 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 772ebcf7-a823-3818-941d-c77c900d6b56 | -9.5109 | -60.52728 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78cc3912-b38f-39be-9cff-f11c97c1a864 | -13.20959 | -50.76017 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cf9fb561-559d-3db2-b03b-7174a83a55d7 | -13.13753 | -57.14415 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1048abe1-1d89-3edb-923a-f2c4abab5d2f | -12.92057 | -46.11303 | 2025-08-18 05:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bdda7635-4310-31ca-aa7d-b48ec61e3f3c | -22.33093 | -47.7216 | 2025-08-18 05:16:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55310b46-6f05-3d9d-b0df-dde4532b9833 | -20.40577 | -54.68694 | 2025-08-18 05:16:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a65be749-1a60-3dd0-8778-97d6b65bdf57 | -19.84341 | -51.20488 | 2025-08-18 05:16:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b5a9444-d75c-3a5d-be4d-4e576116dd48 | -20.87217 | -54.96604 | 2025-08-18 05:16:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72f3e475-56ed-345b-ae62-40c5ba7ad712 | -20.87171 | -54.96973 | 2025-08-18 05:16:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f713dc1-6550-3300-9f65-8c5eb5f648b1 | -20.22104 | -47.02956 | 2025-08-18 05:16:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c18f1add-142b-3752-b6f9-c9c6f84763fd | -20.86392 | -54.96453 | 2025-08-18 05:16:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81274843-e683-38dd-982d-8b5922642c00 | -20.40526 | -54.69093 | 2025-08-18 05:16:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26b7e02b-b662-3428-8ad9-8311a4852d77 | -22.20358 | -56.04276 | 2025-08-18 05:16:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d3d059d-60dd-3c47-b185-52f7d6fd4b9f | -19.14308 | -47.03913 | 2025-08-18 05:16:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| df9fa494-cb42-34e8-ad36-1f86127e4875 | -19.15699 | -47.03483 | 2025-08-18 05:16:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b7e7aac-f9e9-328c-a101-15f978e77f45 | -19.14355 | -47.03371 | 2025-08-18 05:16:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 535a2386-ecb4-3959-8322-80546b31d314 | -17.73221 | -46.16881 | 2025-08-18 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b57d66c-86b3-3419-8640-2048b6d663da | -18.61638 | -49.19744 | 2025-08-18 05:16:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5a069668-bfa9-34a8-8697-e8b8644f1dfa | -17.73219 | -46.17595 | 2025-08-18 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 403b2076-83e5-3d37-875b-653982002b68 | -19.84378 | -51.20153 | 2025-08-18 05:16:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4181901e-e5af-3971-aa7e-94aca0e77d03 | -22.19962 | -56.04224 | 2025-08-18 05:16:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82583a26-2c47-31b4-8405-2ee75f8b55a6 | -18.61679 | -49.19328 | 2025-08-18 05:16:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3b1eac18-3030-34e0-b9d4-e8cc35b3c505 | -20.22053 | -47.03619 | 2025-08-18 05:16:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e608413-6940-344f-8c35-26d429bce572 | -20.40944 | -54.69163 | 2025-08-18 05:16:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78b36dec-230b-3f07-bb67-90883c1bc9aa | -20.87121 | -54.9737 | 2025-08-18 05:16:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 94381c6a-01ae-373b-9916-231f931858f7 | -19.14977 | -47.04008 | 2025-08-18 05:16:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 328c8971-246b-3483-a967-e972a7a82e6a | -17.73167 | -46.17501 | 2025-08-18 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7939df8b-18e7-360a-9bdc-58013b72553c | -22.33043 | -47.72816 | 2025-08-18 05:16:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9ca061b-b541-345f-9e47-13361d6bb877 | -17.73277 | -46.16974 | 2025-08-18 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40e24577-76f8-30d1-8f6d-86d3a7f6c817 | -22.20029 | -56.03691 | 2025-08-18 05:16:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6cb3c8eb-6122-3c87-9d0f-0848655fedad | -20.21961 | -47.03428 | 2025-08-18 05:16:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 290d9106-f61e-3c9e-8bf3-74a73edd44da | -22.27205 | -55.94875 | 2025-08-18 05:16:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0411a7cd-c3b9-3838-bb08-e8aa96ac44b2 | -19.14456 | -47.02193 | 2025-08-18 05:16:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6990092-491a-3d96-abdb-90cc7c235f56 | -26.42167 | -53.23142 | 2025-08-18 05:18:00 | NPP-375D | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d8824c0d-dd51-3ebc-a5e5-1ab87b53f113 | -25.9996 | -52.05842 | 2025-08-18 05:18:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9fd13f8-1a37-39ba-b8ff-c3e48d8210a7 | -26.00328 | -52.05728 | 2025-08-18 05:18:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 18b38937-0f3f-31a6-9d59-4ab40661ead7 | -26.00358 | -52.05383 | 2025-08-18 05:18:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99aef2f6-fde4-32e2-a63d-8d027fe3944b | -26.42194 | -53.23154 | 2025-08-18 05:18:00 | NPP-375D | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 12df24fc-d0b3-3813-b094-53e5926175a9 | -25.99991 | -52.05502 | 2025-08-18 05:18:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d9189b36-7ed9-399c-9930-fb9ba944f093 | -28.83481 | -54.08789 | 2025-08-18 05:18:00 | NPP-375D | JÓIA | RIO GRANDE DO SUL | Brasil | 4311155 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 64d78120-5b82-3852-98e0-f83c0caa6cbc | -13.2186 | -50.7781 | 2025-08-18 05:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 260.8 |
| 745c6e18-3091-3b58-a6fd-3319c4b5404b | -13.2378 | -50.7756 | 2025-08-18 05:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 30125e79-ae75-3d86-9fd1-40874b0998d7 | -13.2382 | -50.7541 | 2025-08-18 05:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 82209cc4-ecc5-3ef1-8c42-177eba5a557d | -13.219 | -50.7566 | 2025-08-18 05:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 32a834a4-b879-3165-98a0-78318258e927 | -13.1994 | -50.7806 | 2025-08-18 05:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 6c62bced-d183-37a7-b608-a3c67f8db803 | -13.1998 | -50.7591 | 2025-08-18 05:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 102ff193-dcfd-37d4-ab11-f55bfc8395a4 | -13.1746 | -54.9337 | 2025-08-18 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 9520d08b-986e-396f-bfda-4ccc414a3166 | -13.2378 | -50.7756 | 2025-08-18 05:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e6dd22f1-ed2f-3020-8727-65e1beb5e1f9 | -13.2186 | -50.7781 | 2025-08-18 05:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 310.6 |
| 9f53eb03-902c-39bd-90a7-2dbf20c37db4 | -13.2183 | -50.7996 | 2025-08-18 05:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5a3528ad-1722-3d8f-872b-99bcea3597c3 | -13.1994 | -50.7806 | 2025-08-18 05:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 966327a6-2b82-33df-855e-836d63e4e6d2 | -13.1749 | -54.9132 | 2025-08-18 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 929d1e40-5b88-394d-bf0a-8c37cb7b1792 | -13.1746 | -54.9337 | 2025-08-18 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 19451351-7a2a-3155-9bf6-7e777cde47ec | -13.219 | -50.7566 | 2025-08-18 05:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| b1506781-982b-345b-99bd-344b62b900d4 | -6.13555 | -57.93533 | 2025-08-18 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3393472-8560-3554-a801-5a33715556d0 | -6.13613 | -57.93137 | 2025-08-18 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe99ddff-3c70-3d33-bce3-4aab00cf898d | -5.45505 | -60.15365 | 2025-08-18 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d1cd5a6-6984-3f2c-804d-da9fde537c6c | -5.45399 | -60.13589 | 2025-08-18 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06264a38-4860-3b84-b058-0b95345ea525 | -4.91377 | -62.30895 | 2025-08-18 05:33:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 969c64e5-22f4-35b0-920c-2e42ff1ae720 | -6.07666 | -57.92276 | 2025-08-18 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7c289af-a5e1-3c60-ad74-2168045ffc51 | -5.45765 | -60.13645 | 2025-08-18 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f411dcf2-5d0a-3d79-9a79-2438987dd820 | -5.44795 | -60.12616 | 2025-08-18 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1a279e2-822f-3237-93a2-6fe22e73a9ef | -4.91322 | -62.31249 | 2025-08-18 05:33:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bc513b2-e25c-395c-bd06-a853be43a24c | -6.1483 | -57.93709 | 2025-08-18 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 57537497-7696-384a-b76c-f396b0a691e3 | -6.1947 | -53.51964 | 2025-08-18 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eeee742-6a03-3732-97ea-a895b7eb23a7 | -5.44665 | -60.13479 | 2025-08-18 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc22fc1a-853e-357c-846c-bad15ca9c6db | -5.45032 | -60.13534 | 2025-08-18 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e89ad2d1-0909-3a67-b287-0a02417db26c | -6.18895 | -53.51889 | 2025-08-18 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b88ed741-b09b-3e4b-a989-9c56fdd24dd4 | -6.13187 | -57.93084 | 2025-08-18 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9da96b2a-a66c-355c-b25f-82f051a141c6 | -5.4583 | -60.13214 | 2025-08-18 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ba2a1d4-e681-3343-9d6d-d66ac1185d91 | -6.13129 | -57.93477 | 2025-08-18 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5802a9fb-9f26-3a94-bd7b-5b3c4736a492 | -5.45871 | -60.15421 | 2025-08-18 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe3861c1-f935-3939-880e-b7a0b7a6b8df | -6.1884 | -53.52288 | 2025-08-18 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa11e357-5926-3f39-b49a-e7df7936f1ad | -11.85326 | -51.5853 | 2025-08-18 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README31.md)
