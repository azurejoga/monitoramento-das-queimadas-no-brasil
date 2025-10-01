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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| decbd2d2-2da1-3f16-9eca-0d2057aef9d7 | -16.38393 | -47.05913 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ce015bc-5a63-33d2-8a47-18fb1a252d95 | -12.21727 | -47.79653 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3a2c20f-dbee-31d2-a8ce-6b0862a8e5e2 | -10.75161 | -45.37217 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec547759-4619-3101-9ea5-a6bd1aaac41e | -12.85122 | -46.95118 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e25fe41f-f54e-3679-bbd8-26cafa06b4ef | -11.84642 | -44.997 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bdf96254-93e3-3529-a003-0594cae6775e | -14.35865 | -45.90787 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7866441-55cb-323a-ba35-84819694cc9d | -12.33888 | -43.70792 | 2025-10-01 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7c3a737-5337-3b64-b327-e50b48a18c28 | -13.30024 | -50.66701 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fbe352e-c00c-3a80-92f5-24b3707b0f5d | -11.52901 | -43.54991 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 656c3e41-bc03-3fe2-9404-863497a5bcfc | -13.64113 | -47.2071 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b2dfc2-63a3-3a25-bee6-67279620f135 | -11.06338 | -47.8209 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54e67793-9bc8-3b89-8abb-75be8911fb61 | -10.8387 | -46.65631 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49f53eba-4994-39cb-a6be-0c33081194ab | -9.82483 | -48.26464 | 2025-10-01 04:21:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cafbcc6-6c4c-3601-87da-3c91ced48131 | -15.39557 | -44.97583 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c05e5ffa-1846-3be0-a449-c23af29e5b64 | -10.20995 | -48.20027 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a844f3a-094f-3d20-995a-38c6064b0e2c | -15.17777 | -49.07832 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 07847584-9806-391c-8d38-f924be2ce767 | -14.6123 | -48.30468 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8b4d70d-50fd-3473-bc52-f8e4663bb691 | -13.23311 | -48.44075 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b243c69e-0421-3d55-9344-39c2c952c7f7 | -14.04923 | -47.96962 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c5d3cacc-ec32-38f7-adbd-9843d7013e3b | -15.93927 | -48.12095 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3790a777-36e7-3bb6-bf0d-71c5b7f9e569 | -11.27952 | -47.81036 | 2025-10-01 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fd739a7-30fe-3a11-aac2-e2c6da482e35 | -14.0168 | -46.31391 | 2025-10-01 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c58eb9ac-4595-3a3b-8bba-e53315238fdf | -11.4676 | -45.0065 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 756ea779-a859-37b5-a576-8cf368b2acd8 | -14.67334 | -48.13172 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 401898e6-ac98-337d-ba10-d72a4186a3a0 | -11.56973 | -50.17942 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8391c9c-9131-3c67-8632-0490ab503608 | -10.66402 | -48.53102 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f3f69edd-1024-3758-9bd3-ded65bae9eb3 | -10.92426 | -46.50338 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bcfcc80-c530-38ae-b13a-dfb300cff3d9 | -15.34261 | -47.93288 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d46a787-1b75-3e14-b350-e7ccee8d3a6d | -15.54259 | -44.33439 | 2025-10-01 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 6a8a1943-0564-36c0-bfaa-b38ce9288081 | -13.34204 | -48.14442 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07e32e4d-dc05-3c67-aaa2-42ba6e5cfc82 | -14.67881 | -46.95327 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fba6929-5804-3694-9875-91673d425061 | -16.50739 | -48.58646 | 2025-10-01 04:21:00 | NOAA-21 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77aa8dbe-693e-37b5-80e9-616f350aff82 | -13.35622 | -48.14301 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9063172f-524c-37b2-a4dd-d183be42c6a3 | -12.92682 | -54.72821 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c4a4bb6-219e-301c-9f35-3e0aeff2a554 | -12.01024 | -46.63079 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c1e49db-b4de-37f7-8d0b-b70a4be87247 | -15.29155 | -46.40629 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39d5205f-baca-3201-971b-b80eeb8f4e9d | -16.27993 | -42.5389 | 2025-10-01 04:21:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 178e3c6c-72f8-3d70-b521-4cfc37548b14 | -10.62833 | -48.59256 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b32ca180-f4fb-3422-b7e5-549148c558b8 | -15.3681 | -47.07185 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6d22548-fcd9-34a4-b275-c2934ad26b3a | -13.97261 | -44.88521 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0236759-5498-3018-8eb7-d3cb97af214d | -10.90646 | -46.55115 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 26728a14-7529-3fb8-91f6-d53d55bcd40b | -14.59324 | -48.29379 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3bb0495-b7cd-3a66-8092-b36d5c624169 | -17.41086 | -47.12483 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2216bd8c-0eb1-3616-b211-dff55f7ad277 | -15.26958 | -48.78058 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a57cd061-58b9-3759-aa4c-ed8ec3756f68 | -15.0065 | -46.96784 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbf99e84-ef95-3d3c-84b1-78633944537f | -15.27093 | -51.47428 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dd9825c-2599-35da-b469-aa9e511a60a5 | -12.76792 | -46.87558 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd9defb1-abc5-3d28-b79e-0cf28f42e9e0 | -11.08887 | -47.83687 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2695312e-090d-36a5-b5f5-3ffad6b724cb | -10.82916 | -45.37371 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e995dc6e-6b1f-39a8-8b9f-be5eb4188c33 | -11.4767 | -45.10238 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 029d2f16-5125-394b-be61-e5178d3bd1df | -15.4799 | -48.55223 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c392d11-917b-3ab7-a37b-9e6c7f08133a | -13.31153 | -47.22483 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f98c034-9549-3f4b-a752-e96033cbfebf | -14.68753 | -45.19243 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e8b7170-563c-3ccc-ad3c-4bdb8b47e8cb | -13.22631 | -47.33201 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac6471f6-3c6c-342f-ad77-1e7cb80a036e | -12.80617 | -46.89267 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92bb0467-0f99-3620-b030-3bdaf06bbfbe | -11.80959 | -44.90313 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1380ab8b-1fc8-3c70-8520-cf89f9700c4c | -14.43582 | -46.35393 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cfc631cf-8dec-3b4c-bcb7-0f21395f4685 | -10.90972 | -46.5734 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ceffaaf9-1da7-3364-8106-aef17a5b1b7f | -13.73064 | -48.81475 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9483f543-9b04-3a01-855d-b4314c38ba8c | -15.245 | -49.71316 | 2025-10-01 04:21:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbde2fe4-9a31-3b22-a2c2-95c4396cf58c | -12.84763 | -46.86679 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51a1cd46-8c5b-3056-9323-14c8e0356347 | -11.65946 | -41.53989 | 2025-10-01 04:21:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 805a28d3-cfce-3400-bf62-6d993592f115 | -11.9964 | -46.65388 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f8e78f2-e1dc-3139-803b-c50b36901893 | -15.76998 | -43.70387 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e05805dd-5573-3f02-bb35-82d9c5bf6518 | -15.27628 | -49.28971 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2defef8-b832-3e9a-aa82-58ff8ea20c7b | -15.54697 | -48.18554 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b63271f-856d-3c95-8e28-028db915b2d9 | -14.96715 | -46.87386 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d0f6397-2e9a-354b-af67-cbd81da14cad | -11.96511 | -46.59451 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3482e01f-2659-37d4-b83a-ac117957792b | -13.16651 | -47.38504 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84c0a988-f7b7-34be-99c4-4c268bf135cd | -14.68776 | -45.283 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4920301c-a06a-30c3-9743-8c83e017eb9b | -14.52381 | -53.12295 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91c74b22-c40e-3deb-8d93-17c59f989be4 | -16.4076 | -47.05943 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd40c9c4-d69b-3506-b772-1769db4c806b | -12.38034 | -50.19969 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7dd2904-cfaa-3056-8602-985e8ae16d0f | -14.09975 | -44.30815 | 2025-10-01 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a0f0dcc-c5a5-3e11-9acd-0b848e38d46c | -10.9761 | -46.54073 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63aa2a3c-6970-3203-9f41-d002ccb86590 | -14.35701 | -45.91854 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1a0027a-a584-3a21-a522-011074c85f1a | -15.53781 | -42.66183 | 2025-10-01 04:21:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0d184c1e-0ae2-3437-8786-062b54753aca | -11.46264 | -45.01665 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c401cbf-b3c6-35fd-b3ce-e89f03b4a969 | -15.16448 | -52.81024 | 2025-10-01 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14ffe0b1-8c9d-3714-b8bb-ebb0d018156f | -18.34091 | -41.80775 | 2025-10-01 04:21:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 60ffd202-4688-3d78-8028-f4259fa0d4b4 | -11.47561 | -45.10947 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 66bc8dea-bdac-355d-aeca-f732258da15b | -13.09549 | -47.04289 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a3e065c-e9a2-3647-b523-3653a8be37fc | -10.77304 | -45.36481 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 790d6531-c008-3df6-bab5-e3be2395585c | -11.76063 | -46.87331 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21678bc7-61a7-3a3d-8740-8526f51a4985 | -13.76923 | -47.95636 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03311706-28b6-3fb3-8803-ebcc44c084f6 | -15.1271 | -46.45633 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ef73761-e91a-3c9d-a9c4-6bed0d47b8f9 | -14.35207 | -45.92868 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a66a45a-7ee1-3142-a8e3-eb2220f8f58a | -10.91047 | -44.26448 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be57f4a7-63c9-35c4-be34-b0f7c3c9c2f2 | -14.54873 | -48.24769 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5a34d03-3031-3e22-a95f-a4c628f55389 | -14.6105 | -48.31573 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f255244c-341b-3019-ac5f-3f6db0562a70 | -15.40751 | -45.647 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62bde821-cd9e-3077-8b22-cea507de675b | -11.14953 | -54.30535 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a4def597-756e-343b-bcbe-cd7c2ef51b50 | -14.41026 | -47.1451 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02dc9c1e-d495-35aa-8cf9-6f3e6c4589f8 | -15.28051 | -47.83309 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daead78f-000b-357a-97a3-bdd461fb89f7 | -14.75474 | -45.76221 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29b9c300-1ea3-336c-adec-3e6ab2da6ed1 | -13.22783 | -48.45142 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28b6f514-a4bd-3667-bc2d-a61452db6103 | -15.29855 | -47.86967 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7e0b46a-363f-3514-ab80-a14456c8cf71 | -14.78198 | -47.50372 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4020e8e-8df1-3838-bb3f-7b59e2648684 | -14.60719 | -48.20804 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 880bf923-ae8f-36e5-b44a-b1f15d6fdb52 | -12.91851 | -47.17048 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README72.md)
