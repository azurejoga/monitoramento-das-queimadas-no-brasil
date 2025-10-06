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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f405444e-dc38-3e5f-8289-b3b7919fc2fd | -15.20839 | -56.81961 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce9b385b-2d78-37b7-a3df-0abcaea66b3c | -15.21836 | -56.83083 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd28c778-43b8-3f4d-8e9e-91900bcfab94 | -14.61432 | -52.50804 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9a8376d1-e640-3c75-9749-ea830bc54128 | -11.48093 | -59.0926 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac7028ce-b4c5-3169-9650-66fd248f34a2 | -18.25489 | -53.32688 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 760bcafc-0ad1-3475-b967-d4082bf84e6a | -14.9148 | -46.85641 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc3fe1cb-981b-38cd-a504-b37217f15bd1 | -18.24731 | -53.34923 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1760d90-fec7-3e3a-8d80-d3f7fd1cb99a | -15.99053 | -56.01125 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b7fd3182-46f8-3d6c-8627-5939a3e50be5 | -18.17834 | -53.36785 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1b836157-c4cd-3558-a62f-5893c5d5a2ec | -14.55287 | -46.65395 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f597307-3b03-3bc8-b414-a0f9e05733aa | -14.90159 | -51.49897 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e762f13e-c155-35bf-9914-4391f0cf5490 | -15.60185 | -52.54683 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f76acf95-1ccb-395c-ad81-e6f239639008 | -18.17907 | -53.38025 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f52860d-9d44-33d9-890d-9192d12232d2 | -12.91832 | -47.29415 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c2730db-4275-30a9-9c9f-95ff1609acf8 | -9.98439 | -67.57332 | 2025-10-06 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 118859f3-efd6-3210-8067-7e0d58fbaff7 | -13.3592 | -48.0498 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91732ba9-0024-3a8b-958b-ecb2ec1a4852 | -15.34901 | -47.99041 | 2025-10-06 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19efd624-5950-320b-8f48-2571a59eb855 | -16.00521 | -50.84612 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 738c6082-3722-38d2-b74c-ed0ebf9e97e4 | -13.26142 | -47.85554 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| da04915d-5e39-3342-b877-dd497f13c466 | -15.6176 | -52.54114 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1441ad96-e156-36e0-926f-439f69bbf4c4 | -13.13371 | -48.00481 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0146252-86df-3e1c-97f8-e4e42922bafd | -12.89887 | -54.75891 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb428126-b8a0-3b12-abc8-532ba4c4e4bd | -13.33201 | -48.05764 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed4e0aef-a9d1-33ce-8924-55b6890dc9cd | -15.65831 | -53.83683 | 2025-10-06 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 942c11d8-f1e5-3b36-89a9-bad7fc680e4b | -15.99392 | -55.98619 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 32e32520-04cc-38cb-b5be-5eef032cd38f | -12.44717 | -54.40591 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0b3c8737-8a04-3417-9c48-5478bc8d5be6 | -16.14946 | -57.57483 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1eda9ecf-77e5-3604-a666-84201ff13798 | -12.37652 | -63.73511 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d596c419-0bca-3c81-a45b-49a3881455dd | -11.82646 | -60.48372 | 2025-10-06 05:18:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c0af518-8278-3aef-8c86-10418916d8db | -13.60584 | -48.69966 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2171baac-f2d9-3593-bad9-cb7f8c20c07a | -14.32227 | -52.97572 | 2025-10-06 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 701b1041-62f8-37dc-b6a7-58670db92e4b | -17.26398 | -46.9177 | 2025-10-06 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0be05b22-0581-3298-b595-a159d16beed0 | -13.25667 | -48.49927 | 2025-10-06 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ae077bc-6003-36b8-bf80-45b23dd6c50e | -13.12719 | -48.0043 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20ae03f7-9ec4-333d-81bb-5c2463abfdd1 | -14.90651 | -51.50304 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 20831954-b6bc-35be-b46d-45d502f8b0bb | -14.86734 | -51.48011 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 232c51cd-9ac3-3c1b-9160-e6b423ef6fda | -13.62925 | -48.71767 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b973806-be48-3b9c-bb3b-d553c93b6ada | -14.6945 | -48.36648 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c898e655-d091-30b0-940b-7bf8540c820c | -13.08105 | -47.82266 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 028d9e1e-829e-3f81-aad1-96c92a644635 | -15.99502 | -56.00824 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3ac59a3e-22bd-39a5-855f-7719663601f6 | -18.11795 | -53.4171 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 648b543b-8b7a-3c22-9127-d0bd18f6350f | -12.31836 | -55.12324 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9410a93-fbbb-3a53-bac2-7cb22fbed632 | -11.87365 | -57.82064 | 2025-10-06 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfff3352-cdca-3107-b087-ea28d97aae28 | -15.9885 | -59.53573 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6817b13-8124-399e-a360-9ad0f66f961c | -16.02517 | -51.06092 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6ef7355-c7d3-30eb-8697-8cfda1882278 | -14.34449 | -47.67234 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39defb2e-6870-331d-b8ba-4215eef6bfa3 | -14.91648 | -46.83947 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7949e53-0386-3a89-8b33-e94317c93be6 | -13.08717 | -47.82759 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08cb758f-5a7d-3278-86e1-0ca673af11cc | -14.62921 | -52.54985 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 329d3cc4-d73a-3661-8feb-02752f65969b | -17.3831 | -53.59548 | 2025-10-06 05:18:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| adb73db5-7236-3eb6-aaef-f28da8192921 | -13.08192 | -47.82587 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ffdc5aa-0907-3fb4-81b3-5983ed37fc9b | -15.57241 | -52.45175 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2681405e-d073-37d8-91b3-d47e4b0df2ad | -16.00204 | -56.0165 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7f2f5800-c875-3166-aacd-8f889e30e169 | -12.32442 | -55.13865 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10995125-f85f-3540-a93e-604a41007acd | -12.38018 | -63.73577 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 835bde6c-0f0f-3f62-b718-befe0742ad3b | -12.31484 | -55.11907 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ace9a041-19b5-3906-a385-9b1effb45675 | -13.36007 | -48.0442 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fd276131-f57d-311b-afbc-3fcbdbd7bfc6 | -18.25211 | -53.35088 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1da55065-6f85-3102-959a-7ac26bdb8294 | -14.34971 | -47.7225 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 617e5a8b-d977-3d6e-aaf0-9657af19f6a7 | -14.9179 | -46.82516 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ea4f6055-3644-3c15-88ee-0a63c213eba4 | -13.69257 | -47.33493 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b876a82-6d13-387d-ac19-37765e3a0a14 | -15.99356 | -50.93569 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 948e5c8c-9e5d-3b3c-b5ad-6a5e0d21adaf | -12.31132 | -55.11488 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02c58801-3fa5-39e2-bfc5-32458292366d | -18.25 | -53.32597 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45655b9b-9ef0-37d7-80a5-88376a034845 | -16.94333 | -52.67866 | 2025-10-06 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64905085-6c65-35c9-926e-1d55ccc22f71 | -17.68 | -52.24631 | 2025-10-06 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91e2951c-891f-36ad-94a5-2c21222f4201 | -13.33261 | -48.05223 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2d9b1b2-65aa-32a9-a018-c21c90e99eb1 | -14.32574 | -52.9868 | 2025-10-06 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e01d5a4-5d26-3362-aa3a-1910f8ad00cc | -18.14485 | -53.39903 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1ed447f5-f5c1-3f9e-85d7-91053223cfdb | -15.61189 | -52.54781 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 80307265-02e1-3fb3-a022-97ef8d19f079 | -15.99405 | -56.01537 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b83f4ae9-c825-3275-85a3-d82a06c7d92b | -15.57207 | -52.45454 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc94e8c8-8d2e-35b4-bb27-430f8e7cc14d | -18.11307 | -53.41641 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3265d73d-1260-3ed9-9835-797bb0e8542f | -14.67688 | -48.40523 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7f7b5a25-611c-3a04-bc31-77472a928828 | -14.71174 | -48.38972 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4d89769e-6e87-3657-be0b-b075993aca08 | -12.98546 | -51.04621 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39fe8cf2-9677-32a7-af58-bfecf73bbe0a | -15.82592 | -57.43633 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 181f50eb-ace5-3613-a748-bd262ce6d886 | -15.22005 | -49.28877 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 00f75d47-fcff-3396-aa3f-d23c63de72d6 | -18.10888 | -53.40978 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 106e0ae3-bf31-37b4-9050-4aa8c1a7886e | -12.45195 | -54.40248 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 713007eb-b008-3755-9b24-56522d752121 | -18.18465 | -53.37481 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c06347b-b025-3bfd-8356-5f33bd9ff83f | -14.69401 | -48.37125 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5a4e1d38-9ceb-35fc-9c0a-962821282283 | -14.60513 | -52.50092 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 78c0072f-4b10-371f-bebd-09d35ccaa8e2 | -14.69267 | -48.38021 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 57562fcc-f1a1-38ea-9f23-30444fe9978f | -13.26703 | -47.17897 | 2025-10-06 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4c2c7d8-a01b-3e21-96c0-3574887b2805 | -16.45458 | -52.16158 | 2025-10-06 05:18:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e779caf7-fbf2-312a-ab57-cb4d81a08409 | -15.60624 | -52.55275 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ea568941-aa1f-39af-bb41-2a289c777027 | -14.71446 | -48.36338 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf682e99-1994-3f3f-8ae3-3453bdfe5305 | -11.67953 | -58.92976 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 56229ccc-9312-30f1-be49-3f9de6a40c28 | -14.86939 | -51.50789 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e542245-2c18-3774-a18f-46a3395d8919 | -15.9795 | -56.00238 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8bf89ea8-5c1d-344e-9b43-e5ae6ef06d63 | -12.98588 | -51.04281 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f55fa13-5ea0-3cb0-a84f-8ffa1bbf1958 | -12.38169 | -63.72697 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 48b0c075-163d-3d16-ba9d-2478b63b2b46 | -18.14044 | -53.39428 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a756dea1-d62a-31a1-a669-7214b3910b30 | -16.01094 | -50.82597 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6028b475-e50c-345f-b18e-99fcfe1df04b | -16.44905 | -52.16384 | 2025-10-06 05:18:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d76c0813-32a5-37aa-b55e-4164d4973eb4 | -14.9012 | -51.50237 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 453fe165-6c8e-387d-8cfe-7556ca2459a3 | -13.08645 | -47.84426 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be369755-f528-3171-8b02-3b9462420e0b | -13.26412 | -47.84271 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed1b6fe1-2c93-3cac-b1ec-ff1e63e8b820 | -13.33239 | -48.05719 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README74.md)
