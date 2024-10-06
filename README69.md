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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa6d4bc1-c98d-3cec-a64f-96890f58f706 | -5.06042 | -42.75501 | 2024-10-06 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 490f3b01-3fcb-3bd5-b95f-ab2b9a1fcb34 | -9.94994 | -44.10224 | 2024-10-06 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcc29ea5-f0ca-36b1-b575-20ad0414d947 | -9.94713 | -44.0981 | 2024-10-06 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ba03bad-4251-33a8-9a3f-f01ce359b0a9 | -9.94658 | -44.10172 | 2024-10-06 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 316dfa5b-534c-375e-a4cb-d068fc23ae08 | -9.47925 | -44.04797 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffa9d26c-ced9-3cb0-be8c-374ee6705d5b | -9.4787 | -44.05159 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e9dc892-dc99-30c7-ab66-382db27cb8f7 | -10.16135 | -42.9007 | 2024-10-06 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 330da0b9-f601-3c7d-a4e2-74bf4bb31449 | -10.24856 | -43.59199 | 2024-10-06 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f979802-649f-3bd0-8478-02b44e1a421a | -10.24799 | -43.59573 | 2024-10-06 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f556f7f-fa10-36b8-9a17-2666f1e32bf0 | -11.73092 | -44.50139 | 2024-10-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a9d2e40-1c82-3adc-a885-c9f4e2ce9db7 | -11.72309 | -44.50759 | 2024-10-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c72c7576-5520-35de-9587-e1b33f414ac4 | -11.72253 | -44.51122 | 2024-10-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98145f08-6771-3c61-9e78-96e7ac991a24 | -11.72028 | -44.50344 | 2024-10-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9c0a8ef-1b72-349c-b17c-e0bebfdb761e | -11.7578 | -43.34568 | 2024-10-06 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed471311-6e7d-30c9-aa80-c1d1d3de645a | -11.72645 | -44.50812 | 2024-10-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b39dff69-c085-33ef-b850-9d81f74b49d1 | -11.73036 | -44.50502 | 2024-10-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54b3a94e-ef59-36a1-9574-cb2ab147fe4f | -11.71973 | -44.50706 | 2024-10-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8393d4c8-da62-3ddb-997a-b7fc07a54b69 | -13.09658 | -44.70892 | 2024-10-06 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c50505de-ccec-3b1c-99b9-3af45b4818fb | -12.43174 | -43.77438 | 2024-10-06 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cdd4318-00ca-31ba-a6bc-dcbf265c3d27 | -13.57256 | -43.67519 | 2024-10-06 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea1c296d-8393-3992-af43-1894947154e1 | -13.48347 | -43.66681 | 2024-10-06 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2e00017-3f19-3488-8fdc-fe9f0d07317a | -12.50011 | -44.83619 | 2024-10-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3740a64c-6289-397b-b464-3c7de8ccbe69 | -13.35644 | -44.54023 | 2024-10-06 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db124128-5c40-3ba8-ae9f-5a1cfea38727 | -13.09602 | -44.71261 | 2024-10-06 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd6ca234-f6b8-34e0-8869-15e91970651c | -13.02107 | -43.83741 | 2024-10-06 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c69bdc3-abb6-301f-9816-9e4b06287349 | -14.69499 | -45.12878 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d262ea72-f074-320c-87b3-739a322a7f2b | -14.69444 | -45.13244 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6197999f-ffe4-3cc2-9cbe-fdfe56fb4464 | -14.69836 | -45.12931 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52e47a5a-d6da-3d93-9128-a9da0bcdb9fe | -14.70173 | -45.12983 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a6384869-50ef-343a-b7d3-dca93cd71739 | -14.70117 | -45.1335 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87fd7d5e-9d8e-3c16-861e-21611e4f0559 | -14.07671 | -45.15232 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e005d38d-1955-3959-8c9a-a6e2c0250f61 | -14.07616 | -45.15596 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6befe89a-1ab9-3d80-bbba-73705ad5da0c | -14.07336 | -45.15178 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf859fce-a74f-3200-8298-fab5797cc4f7 | -14.07281 | -45.15541 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8f5ead8d-1cda-312f-a86c-df7180a2186f | -14.07226 | -45.15905 | 2024-10-06 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9d89917c-9be2-3b35-9b3c-4d981d95031d | -14.69725 | -45.13663 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68c996e3-e940-3c75-91e6-a2c1ee0bccaa | -15.0536 | -44.11254 | 2024-10-06 04:19:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb2184b-c1be-3197-ab7a-fc1b3740f080 | -15.05301 | -44.11654 | 2024-10-06 04:19:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8b2b4c3-5d78-302d-9df3-af95239f6888 | -13.99202 | -44.03497 | 2024-10-06 04:19:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a81ee37d-c8fe-300c-9473-0b42c662179c | -13.89614 | -44.60369 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d59e4f8b-3fd5-3ed4-bf30-90ec169098e0 | -13.89275 | -44.60315 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cabc2ae6-6a05-394f-8829-911319afebc4 | -13.88596 | -44.60207 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1bff346-dd2d-39fa-baff-ef4d899dc792 | -13.89558 | -44.60743 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c74662dd-9c82-346b-9344-471f0c7c4304 | -13.89502 | -44.61116 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47dc39b1-311e-3748-aa4e-00eab7067fb1 | -13.89219 | -44.60689 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08c7220f-7dd7-3d8b-a419-8c324ee6bbd4 | -14.48961 | -44.96106 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce28dee9-fffa-3c44-ae53-5877015752f4 | -14.48623 | -44.96051 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9db5e32-870b-37b1-a4a4-c2daf2a3d8c8 | -14.48567 | -44.96422 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a67420f4-827e-329e-af18-e940fa63ff27 | -14.4823 | -44.96368 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37f29a44-34af-32c1-8542-81e7de1730fb | -14.47555 | -44.96259 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c354f6e6-f466-3cd1-a2dd-2c82ea727d79 | -14.47217 | -44.96205 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3748081-8a5f-3d2d-871c-32008d0be5f6 | -14.42667 | -43.78451 | 2024-10-06 04:19:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19964d67-8f94-363d-a8ce-0cfc573229a9 | -14.33512 | -44.70848 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ca109c0-f6bf-31e8-a88d-ee2469280613 | -14.33229 | -44.70419 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a12920d3-e822-3c60-bcec-9930adfa87dd | -14.32947 | -44.6999 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5c76973-f7fd-3982-bacf-c67a5d3a0495 | -14.32607 | -44.69936 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd7bcae3-3ece-3f1d-8003-83a6fa9f0b7a | -14.29886 | -44.64888 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9041ac2a-69dc-36bf-b170-804a354cf001 | -14.2983 | -44.65263 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1930ac51-523a-35a4-bdd3-d3f3d51aa796 | -14.29546 | -44.64833 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edf9ab86-0679-397e-8f0b-29d2242b3745 | -14.2949 | -44.65208 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d7d8db6-3dcb-3e92-9210-8ff987370287 | -14.13422 | -44.72321 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d89a8e4-eab2-3a38-b195-29a60ed58326 | -14.13072 | -43.71011 | 2024-10-06 04:19:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab101a2e-198f-3a9b-8034-beb2cda23560 | -14.08311 | -44.47771 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c2ba3db-ba0a-3f12-9ade-cd18c9d9838f | -14.08255 | -44.4815 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e6d07d5-0cc6-35f7-9376-71144a1b1db7 | -14.07969 | -44.47719 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e37fc5a4-005e-3f99-b8e2-afe0fd694368 | -14.07913 | -44.48098 | 2024-10-06 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 299ac449-4b14-3abe-8cfe-325f27bd1fdf | -13.89331 | -44.59942 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e229571-3ac3-38fa-b06a-c4ed51f5b4e3 | -13.89162 | -44.61061 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e46c3b5-c0c6-3ed3-8806-02a6a6ae9d4b | -13.88652 | -44.59835 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b6b0c58-2015-3059-9fbe-96b81f8ae708 | -13.88256 | -44.60154 | 2024-10-06 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d736708-3db2-354e-852a-545a187645e1 | -16.24458 | -44.29321 | 2024-10-06 04:19:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6eef556c-eb6e-3176-ac9f-d084c8cfeede | -4.98002 | -43.33619 | 2024-10-06 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae8aba71-6f37-31e7-a4db-eb39fe5d07d4 | -4.01626 | -43.24468 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65602b61-f753-3644-bb46-14fd309437ae | -4.01293 | -43.24417 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 24312d6d-a44f-3c47-a466-b65e681942c3 | -4.01239 | -43.24765 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c129ae4-6603-3602-afc8-9a3256356e4e | -4.00355 | -43.26056 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d591678-b4a9-3e6f-982f-84097ad99189 | -3.99968 | -43.26353 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d19a5076-7585-3a16-ab8f-aef47dec1662 | -4.04579 | -43.24924 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31e35ec8-5785-33b3-83b2-758e42c0cfa7 | -4.04301 | -43.24523 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a52a015-dc6e-33de-8386-6a551f2fd32d | -4.00961 | -43.24365 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9ff54e0a-5b12-3966-9c98-2485caa74f43 | -4.00906 | -43.24714 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2daf5089-58a7-3238-9988-a384bbcc62f2 | -4.13847 | -43.72187 | 2024-10-06 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0059e63-9e66-3128-a1ad-f88ac132b4f6 | -4.13516 | -43.72136 | 2024-10-06 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cadccfd7-83c9-34cd-be07-8a1e6664b4bf | -4.13487 | -43.80959 | 2024-10-06 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fff00ed0-b209-3c1a-9837-e7cbdac0cd1f | -4.13211 | -43.80563 | 2024-10-06 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8aae2cd-55f2-376a-bba8-a7b8ad762c35 | -4.13157 | -43.80907 | 2024-10-06 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 685aa614-ee46-3d54-b18e-fdf2fa3a8c13 | -4.13103 | -43.81252 | 2024-10-06 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99cda40a-1fa1-3027-9c01-f36d9e6a8dcc | -4.1288 | -43.80511 | 2024-10-06 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3ad7938-cd65-3c7e-8036-6ddd7e3a3768 | -4.12826 | -43.80856 | 2024-10-06 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1edc57b7-ee65-3cc1-b2f0-c5c4276a772a | -4.04633 | -43.24575 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69a8f889-10b6-3a2b-be7e-a79c8b5f5148 | -4.01571 | -43.24817 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ead707b5-c931-307e-b765-5b53ac296ff4 | -4.00023 | -43.26004 | 2024-10-06 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 567f2749-5d99-3549-a397-b27e36c7a7ae | -4.8171 | -44.35355 | 2024-10-06 04:19:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 685d1b50-18da-3528-823e-ddb0fd33d17c | -3.73049 | -44.24257 | 2024-10-06 04:19:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 763d2953-8209-3dad-bc39-75d9f3c5c981 | -3.72995 | -44.24601 | 2024-10-06 04:19:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b808e91-83ab-326a-bef0-7f12f822c84e | -3.57833 | -44.0673 | 2024-10-06 04:19:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfe5b795-c106-3094-ade4-db6f27dbf39c | -5.39003 | -44.8364 | 2024-10-06 04:19:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee0cff9e-3017-3913-9073-b447f4edd570 | -10.81014 | -44.77335 | 2024-10-06 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28496b46-09c4-3697-b423-2426b0ed638c | -10.80846 | -44.76219 | 2024-10-06 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdac6fc1-37a5-303b-b70f-1b13cc898ac9 | -10.80791 | -44.76573 | 2024-10-06 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README70.md)
