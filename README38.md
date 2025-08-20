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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94f72199-aa68-345e-86c8-83f5bcdbca35 | -21.90135 | -47.22146 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 01724fd6-5c85-36b9-a5c3-f82f4791de45 | -14.77944 | -59.67661 | 2025-08-20 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35895c13-7586-3738-a7a4-1804d261fa53 | -16.34463 | -50.17849 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da828011-f60f-3e25-a0f8-e91bf1caea0a | -20.43908 | -41.5863 | 2025-08-20 04:38:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8263874b-0ea4-3dc4-87ae-be8d423cc756 | -17.40021 | -46.69831 | 2025-08-20 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b44161d0-8884-3d5e-9431-7a27482cbd81 | -20.46946 | -45.07904 | 2025-08-20 04:38:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dc34ed02-825e-317a-9357-58492fe3c5b4 | -22.69081 | -47.33673 | 2025-08-20 04:38:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 088be7b1-1523-3b7e-9523-f8d787f0ddd4 | -22.36613 | -50.40529 | 2025-08-20 04:38:00 | NPP-375D | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7c62ba77-14a8-3478-b08b-ab637c2556e6 | -20.33265 | -51.71157 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de20910c-33c2-3ef4-9aaf-dabfbdc5892d | -15.05192 | -54.83671 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f88eb8ff-a37e-3ea1-91b6-e0039ced4e77 | -16.313 | -50.18419 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 788e5a10-eb07-39ab-af25-04ddfa138ca0 | -21.31761 | -48.67494 | 2025-08-20 04:38:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2102fd11-4abc-38e2-b268-865cb1f38d6b | -20.34661 | -51.7103 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| be9782c5-9679-3961-920a-9e82695accae | -20.33958 | -41.42238 | 2025-08-20 04:38:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| beb117a9-bfa4-311d-a853-ff79e95b48cd | -19.83976 | -47.32634 | 2025-08-20 04:38:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5078d43b-2abb-3a92-93d4-362bed2c7daa | -17.66761 | -54.06207 | 2025-08-20 04:38:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a48c5a0c-4352-3216-82f3-844d734f1808 | -15.00068 | -54.82098 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9a0d42a-d909-3280-9a97-6372a93643bf | -20.34267 | -51.71341 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eb4dda06-8c8b-3689-b42a-17665a34480b | -19.88616 | -49.83964 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 630f8712-e31f-3c40-a50b-653eab63a3dc | -17.0926 | -48.97997 | 2025-08-20 04:38:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4149b105-1385-3c6c-89b5-9a1212f0d57f | -15.02303 | -54.83544 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8643edfe-c662-319b-8c1f-4933a5cd261e | -19.8705 | -49.82933 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a517e97-89a8-3008-a3f9-d909a68b21e3 | -20.08774 | -47.59754 | 2025-08-20 04:38:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 48eddca7-3b59-3bf9-aa08-49420cbcc8cb | -19.5533 | -47.75191 | 2025-08-20 04:38:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b93266de-7e7a-316a-bd1a-f7ad0f42b3f5 | -22.36671 | -50.40148 | 2025-08-20 04:38:00 | NPP-375D | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 258b43fa-b479-30d0-ba49-ff983b0948c5 | -17.05774 | -48.30566 | 2025-08-20 04:38:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 81ea2f7b-36b2-3fe8-b0b1-98a634bff7e8 | -16.34188 | -50.17433 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7ec82a7-a4d7-3640-bb0c-01b1a271ac67 | -15.05257 | -54.83303 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 963956e4-4e18-3bc6-bb20-e76943f3049d | -17.72673 | -46.2262 | 2025-08-20 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6943bf15-2e46-342d-80d2-b908b056e85c | -17.6721 | -54.05831 | 2025-08-20 04:38:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae28c473-c973-3a3e-8625-060b085bea2e | -20.33993 | -41.41907 | 2025-08-20 04:38:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0f7553d0-3c4a-3ebe-9e9e-5ba94bcd5e7e | -16.33019 | -50.18341 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35d74834-3280-3038-8930-9a023b22bb48 | -15.06674 | -54.8469 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 978d48e1-d248-35e8-8913-36203e75ec5e | -21.9087 | -47.25262 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 341f211f-27ec-3ac1-888e-af1e8adafdd4 | -21.89904 | -47.23277 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 911bec3b-eb45-3350-ba21-330962bc8602 | -21.89177 | -47.23527 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 73237110-578c-35c0-a6c2-9f3a9a9db656 | -14.99533 | -54.82754 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e78604a0-ecb0-303b-9fb7-960750fa705e | -21.87759 | -48.20028 | 2025-08-20 04:38:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e95482f8-faff-3d25-86d6-441f721147a1 | -16.79491 | -50.09143 | 2025-08-20 04:38:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 313c1714-f5b8-3c7d-a6b3-b182c60abdf4 | -22.45511 | -47.55416 | 2025-08-20 04:38:00 | NPP-375D | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 61ee2dc4-d1cb-37d2-8a33-63fccbc55092 | -16.32193 | -50.17094 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d00bfce3-66c3-3d14-8651-01630a2faf7f | -20.34327 | -51.70968 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6367f407-2942-31f8-b4cd-ea964c3cc618 | -14.99666 | -54.82021 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d7bca33-fca2-3fe9-9b4e-8e7da960ab05 | -19.87329 | -49.83363 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 787c7296-65a7-31f9-9cfc-2c68d6f37630 | -17.66393 | -54.06124 | 2025-08-20 04:38:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ee8327d-c17c-3a42-988b-4abbcecc4bdd | -14.78566 | -59.67437 | 2025-08-20 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6dc5e0b-0df9-32e2-b14c-20c686dc9cdf | -20.4374 | -41.58463 | 2025-08-20 04:38:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 653f47c3-cdf5-3785-be24-48148433361e | -14.98795 | -54.82236 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3912a68c-be9d-352c-ac2a-696bb48d7e38 | -18.68139 | -48.17223 | 2025-08-20 04:38:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 01f36c3c-d758-35dc-a973-b74ff6db831b | -19.88673 | -49.83589 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| dd916f66-ab03-3d61-a39a-a16bb5e2fed5 | -15.04854 | -54.83235 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ed932f3-e50b-3f2f-9d7f-c1be3a659b36 | -21.90691 | -47.23739 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7063cbef-9907-3d60-8d3b-3c7e52db56b3 | -20.33764 | -41.41972 | 2025-08-20 04:38:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66a3cdc3-74a7-3802-af98-740f7d995a74 | -20.1085 | -44.33881 | 2025-08-20 04:38:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25282ed3-5d17-3b66-b9ee-46318f367cbe | -23.65023 | -47.29017 | 2025-08-20 04:38:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 900f240e-cb57-356b-a728-43ca3f078227 | -20.21758 | -44.13045 | 2025-08-20 04:38:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1cd3bf1d-0a4d-311f-a609-7ddb2e641877 | -18.82971 | -48.56417 | 2025-08-20 04:38:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 265bee06-660e-3f5b-b4e8-7ebdfaeea1f0 | -19.86156 | -49.82012 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2b397497-32c5-354b-ad96-0f9e4ca3b2e4 | -21.89968 | -47.22779 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 54a4a721-ca61-3c22-8429-d9e5a3a55c5f | -22.29506 | -48.54142 | 2025-08-20 04:38:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 10d0b0aa-f5fe-3378-8289-8473fc4a2045 | -18.18192 | -47.89566 | 2025-08-20 04:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fdbaeaa8-928a-3e0e-ab28-f65a89bc549d | -20.33325 | -51.70785 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cc86ba45-57ec-3030-b5d7-bc22d7ef1aef | -17.66841 | -54.05751 | 2025-08-20 04:38:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0c97138-c592-33a1-9ec5-fb5dffbccbee | -15.05998 | -54.83816 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b0be81d-f520-3073-b0c8-38c5ba30b308 | -20.33993 | -51.70906 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4575b750-eb8d-3ef0-bf70-6f4723ca1172 | -15.00267 | -54.81005 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d116ac18-599d-31b8-8b3f-18b898771bdc | -20.33599 | -51.71217 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 803de538-02d5-36b6-8a48-57b9e41377df | -16.32687 | -50.18285 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3a345de-5d80-35ab-b509-09e80789b163 | -18.67443 | -46.98215 | 2025-08-20 04:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6681e9e5-181b-35c4-bc5b-104af5cbed67 | -14.98861 | -54.81875 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f01307e1-9003-3b2f-b4f2-01189f6200ca | -22.36933 | -51.51841 | 2025-08-20 04:38:00 | NPP-375D | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e0f62650-7c1a-360f-9dbb-a63685709984 | -16.26009 | -48.85899 | 2025-08-20 04:38:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16e26de0-9aeb-3082-8fdc-65950b95157d | -21.90789 | -47.22396 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c5ede8b-f95e-3a0f-a091-1db93d2c4863 | -21.89516 | -48.18842 | 2025-08-20 04:38:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb2a9c11-ac7a-3c1c-a727-794d02792242 | -21.90725 | -47.22888 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1979359c-676a-37a4-a6ab-1f2c62a6079c | -14.9993 | -54.80571 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24f06f25-51a1-3af7-98ee-d96a26a97bf1 | -15.04985 | -54.82502 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a072765-7d8e-3b80-80f0-77744d64c1aa | -15.00201 | -54.81368 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 90dbf07a-4eb6-3141-b3f4-32e0ffa8e984 | -21.2146 | -46.95755 | 2025-08-20 04:38:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f0e8f9e-7922-3480-bcf1-9de674adf201 | -20.02518 | -48.11995 | 2025-08-20 04:38:00 | NPP-375D | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cc75907-ca54-33be-b1cd-4380c6c922b8 | -22.6946 | -47.3373 | 2025-08-20 04:38:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15badb98-9895-3693-8c53-9d52d4a43811 | -19.7363 | -47.87725 | 2025-08-20 04:38:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92a6b2b4-fb35-331c-941e-557778833b38 | -16.78929 | -47.97977 | 2025-08-20 04:38:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e57feec8-08fa-3cdf-8a3f-c2548e7597fa | -22.40907 | -46.62004 | 2025-08-20 04:38:00 | NPP-375D | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a5c4993f-aa28-3cb5-bccc-25391a043375 | -16.40046 | -48.88095 | 2025-08-20 04:38:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1274ca69-a972-3fbb-a8f7-cc073dfe23b7 | -14.78109 | -59.66866 | 2025-08-20 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0dd6bc4f-4f0a-30f9-a459-de06a8d4a676 | -15.06336 | -54.84254 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e425ff24-b1d0-3cd8-b756-7d32965a4d84 | -21.90447 | -47.22695 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 37d00bef-4169-38f7-ad4b-59e2dd967795 | -16.18054 | -48.86115 | 2025-08-20 04:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e28aa1b4-5070-3990-8576-927a51057135 | -16.33352 | -50.18399 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6973be6d-b3c7-31a5-a09b-286ebb6ae5ad | -17.55752 | -44.48285 | 2025-08-20 04:38:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b452bf4-976f-36c6-8343-7f0a3c4e34eb | -21.90513 | -47.22203 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 358721e1-1af9-391a-91b6-a7a2353b289d | -16.69248 | -47.63317 | 2025-08-20 04:38:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19eccd42-c671-3965-b357-93f4ce33cb19 | -19.86435 | -49.82444 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 233bb7d4-6781-372a-9526-a0d723c5dd98 | -19.8828 | -49.83908 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f04dabff-7674-3a95-868e-7a6887b115e4 | -21.91163 | -47.2546 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 52a1b435-7dae-34d6-b25a-8b2eba3697c7 | -19.74439 | -46.04032 | 2025-08-20 04:38:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 843715d7-1d82-3b7b-9c50-530d5a54402c | -21.90474 | -47.21852 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 085fa2ca-97c8-3ef3-b380-9ea8540bc158 | -18.5054 | -49.95983 | 2025-08-20 04:38:00 | NPP-375D | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d67b5dc0-1040-31c0-a58d-5498fb9b45bc | -16.25765 | -47.97216 | 2025-08-20 04:38:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README39.md)
