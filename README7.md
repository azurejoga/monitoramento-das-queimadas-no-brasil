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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf3b14a2-650c-3e27-9cd7-58503e45472d | -21.7904 | -48.452702 | 2024-10-04 00:40:25 | METOP-C | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1a8cc786-148c-394d-9fd8-a2d57d1a631e | -21.8064 | -48.748299 | 2024-10-04 00:40:25 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9948f064-bea7-311c-89a9-82cd968d289d | -21.808399 | -48.758701 | 2024-10-04 00:40:25 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 69daa115-ede1-3c5f-a63b-aafdc276cf11 | -21.8104 | -48.769199 | 2024-10-04 00:40:25 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 734b10dc-112c-3d47-b024-c804b144e078 | -21.7966 | -48.750301 | 2024-10-04 00:40:25 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 06f21f89-d428-3c58-9fc0-25f3fa6a4995 | -21.798599 | -48.7607 | 2024-10-04 00:40:25 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 82a4ba25-37d3-3125-964e-bf38db829bdd | -21.8006 | -48.771198 | 2024-10-04 00:40:25 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb00f6b-81f4-3eda-950d-9a44888c22fc | -20.496099 | -42.3652 | 2024-10-04 00:40:25 | METOP-C | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2365d517-4ab8-34d2-b0f8-fcbda4505e52 | -20.4979 | -42.373001 | 2024-10-04 00:40:25 | METOP-C | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f58a6d0e-4ebc-332d-ba6a-45414130ac31 | -20.519899 | -42.8708 | 2024-10-04 00:40:26 | METOP-C | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d23f0119-4cae-3498-9392-e092c9bd0fe8 | -20.521601 | -42.878399 | 2024-10-04 00:40:26 | METOP-C | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfcbd9a2-acda-392c-b8d6-4bb7eedf4148 | -20.523399 | -42.885899 | 2024-10-04 00:40:26 | METOP-C | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a02bb80e-adbc-3ad4-bc11-f9a36e3ab376 | -20.1761 | -41.446201 | 2024-10-04 00:40:26 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8377963-e895-3b87-a553-3d42340c3917 | -20.178101 | -41.4547 | 2024-10-04 00:40:26 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c178429-8654-3b56-8c3f-29ea2b5d022d | -21.790899 | -48.7733 | 2024-10-04 00:40:26 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fd2a937b-8d17-3be4-a09e-5afe6fd4b435 | -21.7929 | -48.783798 | 2024-10-04 00:40:26 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c381527b-1a3a-35f9-afe0-e37ef543a9e3 | -20.437201 | -42.511902 | 2024-10-04 00:40:26 | METOP-C | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c76bf6a6-a209-34c9-9eaf-d41805facc64 | -20.438999 | -42.5196 | 2024-10-04 00:40:26 | METOP-C | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c65f2e32-01d0-3874-897e-67c45bbf4628 | -20.427401 | -42.5144 | 2024-10-04 00:40:26 | METOP-C | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f328adc-0fca-3974-8355-e824077fa184 | -20.1768 | -41.579498 | 2024-10-04 00:40:27 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 967574e4-f4a1-39b0-9d7a-7c07529ce6ce | -21.583401 | -48.4869 | 2024-10-04 00:40:28 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ed082da5-696c-3acc-9b45-ed29488f84be | -21.5716 | -48.478901 | 2024-10-04 00:40:28 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3f35b038-acac-35b1-9f22-7da9ebec4dc0 | -21.5618 | -48.480999 | 2024-10-04 00:40:28 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bd57c100-5c46-3d8f-9c56-b9271fff84ca | -21.573601 | -48.488998 | 2024-10-04 00:40:28 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5b73894f-7e30-3455-bce0-73e874a3f2a4 | -21.563801 | -48.4911 | 2024-10-04 00:40:28 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6c694a34-7959-3287-8fe2-c9c27d38443a | -21.565701 | -48.501099 | 2024-10-04 00:40:28 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d6e99f87-e41a-33d8-8984-7f2525bffbdd | -20.466299 | -43.178398 | 2024-10-04 00:40:28 | METOP-C | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53c154cd-a420-304a-8fc5-813d2ca9165d | -20.468 | -43.185902 | 2024-10-04 00:40:28 | METOP-C | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 52dd5849-e9fd-3564-ad5e-68d0de5f4f0c | -20.454901 | -43.1735 | 2024-10-04 00:40:28 | METOP-C | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f38e71f0-10b9-314e-998d-3e21566ef005 | -20.4566 | -43.180901 | 2024-10-04 00:40:28 | METOP-C | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a79f2250-eda0-3038-a8b2-339c3b1803c2 | -20.4583 | -43.1884 | 2024-10-04 00:40:28 | METOP-C | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77fbef64-5b8e-3e4d-a4c7-73ed51dcd322 | -21.558001 | -48.672001 | 2024-10-04 00:40:29 | METOP-C | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d3308eb9-6fd6-3fa7-8737-c7fd24918207 | -20.4942 | -44.035099 | 2024-10-04 00:40:31 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 813586f2-d26e-33e8-95f0-2284d29c82da | -20.4828 | -44.0303 | 2024-10-04 00:40:31 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| be95d3d9-dde6-3340-a806-7dc74f6cd250 | -20.4844 | -44.037601 | 2024-10-04 00:40:31 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8592a2f8-ddae-3278-8188-948754d7db5a | -20.2609 | -43.183102 | 2024-10-04 00:40:31 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e5fb6f3-41e5-36e1-b7d0-34ab4b7774fc | -20.4925 | -44.027802 | 2024-10-04 00:40:31 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 54c4adf7-ce87-3aaa-9694-1853f5351ee0 | -21.004999 | -46.7612 | 2024-10-04 00:40:32 | METOP-C | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe90c6a6-7ee7-3966-a77d-52e76b1132d7 | -20.2495 | -43.178101 | 2024-10-04 00:40:32 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1672fc7-7879-3de7-a367-28b6221c6bd4 | -20.3353 | -43.556099 | 2024-10-04 00:40:32 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b64c700a-11df-3661-a6fd-acf668990c33 | -20.336901 | -43.563499 | 2024-10-04 00:40:32 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4109cc9f-e30f-3f57-9ba8-d24a7f9e1bfe | -20.2829 | -43.506901 | 2024-10-04 00:40:32 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6681212d-35b7-3a03-bc2d-b9fa60a3fb88 | -20.2845 | -43.514301 | 2024-10-04 00:40:32 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b79e63f4-0452-34a2-9a2c-16ce41f88b10 | -20.2731 | -43.509399 | 2024-10-04 00:40:32 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27c8c211-2082-3074-8f0d-9afbdd7e0f67 | -20.2747 | -43.5168 | 2024-10-04 00:40:32 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94d0b766-ff9c-3648-9d60-c5bf73255f6d | -21.0033 | -46.752998 | 2024-10-04 00:40:32 | METOP-C | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d550b64-cc66-3fcc-b597-d18ab78794ed | -21.3491 | -48.802502 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 62e8a5bd-743d-3ee9-8ddc-ed49e07241b8 | -21.337299 | -48.794201 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b6f46c5-e82c-384c-b861-376dd9ae9543 | -21.3393 | -48.8046 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a2fb1fd-f7aa-31c6-aae8-63f2ed52267c | -21.341299 | -48.814999 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72033ccd-d738-3aa1-9ccc-787f817d9e0a | -21.3276 | -48.796299 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f978ad0-a9c0-33e6-af38-aa83b19220b2 | -21.329599 | -48.806599 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc8ac451-72a1-399e-8767-a63dbc776043 | -21.3316 | -48.817001 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a713943a-f261-3066-9512-cdc6c265d9d9 | -20.5179 | -44.8918 | 2024-10-04 00:40:33 | METOP-C | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8c7c073-5d9e-3f36-bd5b-c5e6e0d99afd | -20.519501 | -44.8992 | 2024-10-04 00:40:33 | METOP-C | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d0e8b80a-d3ac-3deb-8a0f-224f453a2aaa | -20.521099 | -44.906502 | 2024-10-04 00:40:33 | METOP-C | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b570370f-c938-3535-8fb0-cc38b8bdcb78 | -21.3473 | -48.846199 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c38822a7-87f9-3154-84dc-6ab9138b0d5d | -21.3533 | -48.877499 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| df51fd71-d0c6-372f-8f7b-05091acc63f2 | -21.355301 | -48.887901 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bd8da917-b521-33a8-98a2-1457b9bbb4d3 | -21.3573 | -48.898399 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c500cd95-fcf6-39d1-8abf-584937e8dc95 | -21.3395 | -48.858601 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc40e0e-fba6-3109-8b09-ff7ab9958612 | -21.3435 | -48.879501 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6ce700b3-ce01-3562-93a1-2a43e66c1ee2 | -21.3456 | -48.889999 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 69021ff4-f30a-398d-b431-05e96fe1eef9 | -21.347601 | -48.900398 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ee0ebece-525b-320b-b1aa-8578235396f4 | -21.3277 | -48.8503 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 787d5448-24df-3034-8234-8c84be8314c7 | -21.3297 | -48.860699 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5b394141-b2fc-3625-b1a5-5264c4ca7446 | -21.331699 | -48.871101 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8e59e42e-50d6-345a-94f9-161c197eba23 | -21.3337 | -48.881599 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 76e6a25a-c878-34da-a6fa-d87b1ab9d5a1 | -21.3358 | -48.892101 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 83dc75a4-029b-3658-a43c-4dba20004fb0 | -21.337799 | -48.9025 | 2024-10-04 00:40:33 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2b71eb22-324c-3664-b886-dab2c7af3c07 | -20.264999 | -43.519199 | 2024-10-04 00:40:33 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33adf1af-807b-3f8a-aecd-353d1fd17eee | -20.266701 | -43.5266 | 2024-10-04 00:40:33 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d55c7910-4f76-3a62-a7f8-2c72db3c37a4 | -20.2833 | -43.600201 | 2024-10-04 00:40:33 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 945f4aa8-4a81-3fb2-9595-25e48fe60012 | -20.285 | -43.607601 | 2024-10-04 00:40:33 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 933fc605-6cef-372b-87f2-22b0015891c2 | -20.509701 | -44.9016 | 2024-10-04 00:40:34 | METOP-C | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9aa30111-d038-3031-a8ff-ccb9d4b58c82 | -21.308201 | -48.8545 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e37cb35a-1aa0-31cf-b1ae-70e7aff0bfc8 | -21.304399 | -48.887798 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4bc79b25-937d-3f80-8983-458e87796375 | -21.3085 | -48.908798 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b3486a36-3329-3dd5-af71-c23bfbcdb253 | -21.2946 | -48.8899 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e3271be2-f79f-3970-b6c8-573ebe9d4eae | -21.3179 | -48.852402 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5ced10be-f455-3cd2-a479-29ba47232656 | -21.319901 | -48.862801 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 567fd678-c1e4-3bde-8171-5235e49da4fa | -21.321899 | -48.873199 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2917a2f6-4163-3f7a-a24e-5fc88dd1e668 | -21.3239 | -48.883701 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a493e569-c68c-360e-ae52-3bb4f76806a2 | -21.326 | -48.894199 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 45eab343-83dc-3f3f-bc87-48ff9a84c663 | -21.327999 | -48.904598 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7f3f7b33-068d-3fc2-884f-52d7d6d64352 | -21.33 | -48.9151 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ec7d4011-28ce-333c-a101-2ff9d9ba7aed | -21.3102 | -48.864899 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 368d7f73-733d-3f73-a582-a754a6937731 | -21.312201 | -48.875301 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 444b0647-826d-3e62-92e5-5d1d0e1bce81 | -21.314199 | -48.885799 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1ba6d785-0daf-3427-b4a5-187e6963cfc0 | -21.316299 | -48.896301 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b5259add-7c83-3b6d-9459-6e1e740e113a | -21.3183 | -48.9067 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 51150ada-2a67-3372-b620-0c7dfb8d35c5 | -21.306499 | -48.8983 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0749ce69-f1e9-3a6a-9808-c96245a3acca | -21.3004 | -48.866901 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3292ad1d-b30d-3c25-b0fa-bacb534217b2 | -21.302401 | -48.877399 | 2024-10-04 00:40:34 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 78d26805-3494-3930-9a19-b9eaebaf1907 | -20.164801 | -43.396 | 2024-10-04 00:40:34 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d21699c8-6ce0-3570-9463-f09bf066b625 | -20.1665 | -43.4034 | 2024-10-04 00:40:34 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04d2c2a0-ef0e-3fda-a079-cd62f6f65bba | -20.1551 | -43.398399 | 2024-10-04 00:40:34 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11932a5a-3b4e-3a3e-b9c9-ba9da82e1d66 | -20.156799 | -43.4058 | 2024-10-04 00:40:34 | METOP-C | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d930f0a-4276-3c2b-9dcd-165690582a03 | -20.1085 | -43.5117 | 2024-10-04 00:40:35 | METOP-C | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7586bfc-49bf-379b-8ab6-1a15a39f89e1 | -19.857 | -42.373199 | 2024-10-04 00:40:35 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README8.md)
