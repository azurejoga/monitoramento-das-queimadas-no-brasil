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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 240fa7ba-351f-38e7-85e5-72fa032049aa | -14.68319 | -48.24704 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d318958f-cede-3f11-83e4-872204b20907 | -15.23581 | -48.73989 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5155453-731f-3360-b633-49f2978fb0fa | -14.17756 | -46.11674 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 543e5dcf-1b3c-358b-88ef-2dfa487059a7 | -15.23543 | -48.74328 | 2025-10-01 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b1831e3-1269-3161-a335-87bfc788de9b | -14.5972 | -48.23165 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 433e6598-3588-3e40-a347-d8ce9ddb323b | -14.78944 | -60.20185 | 2025-10-01 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f49b0963-3001-3769-8157-c1304e42a11d | -15.00929 | -56.0431 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16daa25f-7a94-3ac1-b698-74713aa3c26d | -14.67767 | -48.12936 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d31e10ba-a974-39f0-8b61-306ef7a3fc1e | -14.79362 | -45.78854 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 23e99916-3e94-3f07-b0ae-286623d6373f | -14.9105 | -51.67697 | 2025-10-01 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aef51753-9227-3a98-b12c-567b5f4d59a4 | -14.14847 | -49.2019 | 2025-10-01 05:12:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 562e5d6f-aab2-3408-bb8d-b9235f4eb111 | -16.37163 | -47.06284 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d55b94b5-bb4d-3618-ab9a-4a1f3119ac0d | -14.60664 | -48.30939 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7162f736-d0e9-3091-8313-76aa55a4757d | -14.69936 | -48.26399 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64e59906-5851-3693-af88-793f0612df31 | -13.69512 | -48.646 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afa32dcf-23fc-391c-91ff-6a39709ffbfc | -14.62404 | -46.9848 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 169c8a57-5726-3f97-b87c-415f6449521c | -17.89139 | -57.594 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1f866bbf-7547-3b3b-8948-21c27824dfd5 | -16.01723 | -59.4947 | 2025-10-01 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03f466e4-efe2-3028-a7e7-3c25c1273a6c | -13.94205 | -48.10379 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e800e864-9672-3796-a1d4-a7281b171e11 | -14.68103 | -48.23373 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aeceec0a-b80a-34ec-ba63-46399f68f825 | -16.19856 | -57.59818 | 2025-10-01 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7b068245-76ab-3085-b4e1-0e11bbd83c15 | -16.416 | -52.16904 | 2025-10-01 05:12:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c6476ad-e4e9-3eea-a40f-66a36c493843 | -15.42027 | -47.05228 | 2025-10-01 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6c883b1-8ed6-3eb2-9986-63a4a7835113 | -16.02298 | -50.90855 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84a5b469-0697-3779-8088-3e2d29a1ce7b | -15.28434 | -56.78741 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24dd69c4-86e0-3e19-a4b4-e3809e3ab1f6 | -15.16149 | -49.09247 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3078c85c-b53a-3de2-aced-1a3eb90a9144 | -18.15883 | -46.11243 | 2025-10-01 05:12:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 092ea7b0-1eb0-37b4-ade6-88c86ba55674 | -14.35587 | -47.13942 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f78bd80-b99c-327b-a3ec-ef47cab12654 | -16.1917 | -57.59724 | 2025-10-01 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 660c7b71-f0a3-349b-a91f-01bc1f4aafdb | -14.03396 | -47.9642 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7710413-4be7-317e-a405-2540395ae04a | -14.66232 | -48.13278 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 002698f4-b130-3119-ac02-3d87abe2bf97 | -15.29549 | -56.78467 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a94c2ad-20f2-3893-92a9-3efa2f69bd4b | -14.90105 | -48.13106 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4bccc5e3-2135-3362-ad7b-f949f4c1942b | -16.19562 | -49.9981 | 2025-10-01 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72f5cbfd-7808-37bc-9413-9939cb2ee8c0 | -16.1906 | -57.60468 | 2025-10-01 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5b8516ae-43f0-382b-9d18-74a2edf92802 | -16.76536 | -51.34183 | 2025-10-01 05:12:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d221c594-646c-39a0-b6f7-56d2eb62d444 | -14.89872 | -48.12857 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39a53696-74fc-35a2-9d91-3b9a1bcce654 | -14.70208 | -48.12727 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3315736-d5ab-3463-9fc8-1405fd3a89a4 | -14.02479 | -53.88103 | 2025-10-01 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 192def3b-f59e-3b1d-9255-b2e13c12eb48 | -16.0013 | -50.8738 | 2025-10-01 05:12:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f73b543-dcee-30c9-89d3-3bc720f02be5 | -15.24622 | -49.71838 | 2025-10-01 05:12:00 | NOAA-20 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdb3b1e7-99da-3179-87b1-4a20ad629132 | -14.87674 | -48.32296 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f8fbab2-7cfb-3b78-8ab2-6588b624468c | -13.98418 | -44.91316 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 978f27f0-ef8b-3fb6-8f20-4a8a2a9688e8 | -18.9065 | -48.069 | 2025-10-01 05:12:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 513d23b8-6e73-3f3f-b77e-b1f1b30557e7 | -14.78466 | -45.80841 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 151ded29-08ed-3851-bc5e-6d6fc254e003 | -13.77179 | -47.95341 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ab2955a-7761-3046-9535-84907e016078 | -14.67691 | -45.29301 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7b87f51-3455-3a6e-88cc-c27b9d2c6ccc | -17.90313 | -57.5747 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e4bad04e-c1a6-3938-985c-4f14e7a373f6 | -14.44024 | -46.3584 | 2025-10-01 05:12:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dbf5054-4438-3ab7-8ff1-a537e39853ae | -16.25353 | -50.9374 | 2025-10-01 05:12:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e1d4a943-7155-331e-86e1-2a8e0c90e9c3 | -17.89445 | -57.58569 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| dfb4bd25-75d0-33dd-a2b7-f1d1ad57e2af | -14.8896 | -48.12475 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 07d184a7-0249-3a7f-9fee-624178b24d95 | -14.18131 | -46.11406 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57ee0064-851a-3395-a95c-59357bbdf5db | -13.98033 | -45.05354 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 751eae53-62af-3c22-9ecf-9830bce4f047 | -18.16003 | -46.11124 | 2025-10-01 05:12:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 09391bae-5f39-3e20-b37b-3970c8082b20 | -16.41164 | -47.05689 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f040225-f4a2-3fbe-96fe-5f6fd48fb6ba | -13.67404 | -48.06983 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d4162f26-50cb-338d-8627-86f98a0791bc | -16.36016 | -49.96824 | 2025-10-01 05:12:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16a8d9a5-0d5a-3c47-b44c-efdd0bcd5481 | -14.19372 | -46.12534 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2031e4a8-ada5-344d-a518-d37cca722ab0 | -14.7543 | -45.76417 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 56f5816f-4491-33b4-8cee-9065a0870210 | -14.52149 | -53.1207 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f0e7836-8a08-3a6d-9aed-2c23b9c051a7 | -15.13551 | -48.01332 | 2025-10-01 05:12:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce3906dd-bb46-3d31-ac5b-781ec09f744d | -14.18543 | -46.10675 | 2025-10-01 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f9c136f-4372-3eaf-b8df-92c7de642c8a | -17.89504 | -57.58159 | 2025-10-01 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| eefdb3c2-1d3e-3d82-b4d6-6d40d713b212 | -13.67305 | -48.07858 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e52b6059-ea27-3e37-b79e-0ed3075e429e | -13.67014 | -48.05115 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcc99751-4edd-35e0-b3d0-31efce65d25e | -15.16753 | -49.08967 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c8e5879-2fae-3329-9f34-3f74aaabc87e | -16.2481 | -50.93978 | 2025-10-01 05:12:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26416f4d-871b-31ee-b532-a326c3c12532 | -13.76469 | -51.22306 | 2025-10-01 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 77e10800-516e-3b0b-bac3-a564ac815402 | -13.67058 | -48.04726 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f7b4cba-9288-384f-b70a-0784d49a36f3 | -14.71059 | -48.13354 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a6ef423-bc3d-3f37-a80b-668c04e9e187 | -14.89731 | -48.10909 | 2025-10-01 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 50a46ad7-db35-37af-84d5-2e73aea6a586 | -13.92915 | -48.11155 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33a3e252-b5bb-38f2-9ee1-6610e1109783 | -14.75366 | -45.77068 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d120b25-28df-320a-b160-791c318a1a8b | -16.75971 | -51.3473 | 2025-10-01 05:12:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 585db1c3-e390-30d7-a5b9-6e268db2c71b | -14.68541 | -45.27983 | 2025-10-01 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 278bdc0a-c8ed-377c-be9b-1d63513e24f4 | -15.28785 | -52.89627 | 2025-10-01 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20374e3b-547b-389c-aec6-7db76680c26d | -14.62965 | -46.97873 | 2025-10-01 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea068b1f-5b30-3d82-aa0b-f04fd56b6740 | -15.26794 | -49.29016 | 2025-10-01 05:12:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1858b9d9-f116-3edc-8770-db2e49143577 | -13.91389 | -48.08753 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f89eda7b-0f23-36ae-9812-71a0058e4642 | -14.86712 | -49.7153 | 2025-10-01 05:12:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec6a4d29-5ee5-3c4a-987c-289a508883fd | -16.25317 | -50.94044 | 2025-10-01 05:12:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dcfbe797-faea-3fc3-9145-ccd6ca013377 | -14.02325 | -46.32364 | 2025-10-01 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d1439b5-a091-3f1e-915e-4fbfc38939e2 | -16.41164 | -47.05913 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21484439-e8a6-3bb2-9ae7-9bbe79e3d3cf | -13.78326 | -47.98791 | 2025-10-01 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbd0469b-24af-3e36-bb7a-7b668e142495 | -14.70025 | -48.22338 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a55ecc8-d1d8-35e4-9043-3835afc66fe7 | -13.93407 | -48.12088 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6b012b1-7d99-30d7-a4ae-3d9e5b758be4 | -14.98717 | -46.96975 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33c2e972-9383-3531-bd4b-22d1142eafbe | -16.19513 | -57.59769 | 2025-10-01 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0ca8a9d7-8765-3ed7-87b6-f16fea0e907e | -14.68516 | -48.11583 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68b1b009-eacf-3405-85e0-be546c3a74dc | -15.3058 | -56.7934 | 2025-10-01 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7925485d-f91e-3bcc-bca3-3bc0bd534b5d | -16.40506 | -47.05697 | 2025-10-01 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee131334-8116-3ae3-a03d-1d1a25e6e660 | -14.54599 | -48.22421 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2e29d89-9673-366d-8d37-103c79ca1b66 | -14.52575 | -53.12135 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1601de59-7086-3f76-b408-922a78e2531b | -13.69731 | -48.64599 | 2025-10-01 05:12:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ecc046c-db2f-3751-9381-b6a5a0f3d72d | -18.96208 | -47.87504 | 2025-10-01 05:12:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be2a8726-4715-3359-9f4a-442dc464dbe6 | -13.91438 | -48.08323 | 2025-10-01 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 653a1747-d766-3abe-8aae-e1b47c5b475d | -14.88032 | -48.3264 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e80b1592-5488-3e1e-902e-b1f307bf1b13 | -14.89747 | -47.21202 | 2025-10-01 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45c5c569-4d79-33ef-b4b5-270f216a7307 | -14.60565 | -48.31834 | 2025-10-01 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README137.md)
