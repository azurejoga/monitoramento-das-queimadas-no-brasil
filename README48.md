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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4796a815-25ec-34e9-a350-0e4144ccd83b | -8.62569 | -69.71965 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c7a6e72-a8fb-3ecc-87a9-b99a10b19d95 | -8.62492 | -69.72424 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58630e86-581a-3884-a4e6-1d8e826cce09 | -8.62194 | -69.71902 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11418044-ece1-32fb-8515-0baf1f1beae5 | -8.62116 | -69.72363 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6687cfce-d971-32f8-b48a-df6c46cb6ac0 | -8.49256 | -70.09594 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddf68b61-990e-3667-820b-389e4f5c1bc4 | -8.15124 | -70.16111 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11bce018-91ad-38d4-92de-095b43a5b5c7 | -8.02149 | -70.07193 | 2024-10-31 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3c0c1c7-9c12-387c-be00-85862c57a78a | -10.92245 | -69.32745 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5fff96e-03a0-398d-ab02-b5ca49c7d8ea | -10.88996 | -69.39018 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11fd9f05-7e09-361d-9d0f-fcb71569c0e7 | -10.8661 | -69.5331 | 2024-10-31 05:44:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83999cbd-af3d-3c07-b7e9-8db8434714e1 | -10.77562 | -69.33369 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e667f142-f556-3b9e-a986-98811ab510eb | -10.75805 | -69.41658 | 2024-10-31 05:44:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf023fed-bcb6-3421-a378-ab25951f5812 | -10.75445 | -69.41599 | 2024-10-31 05:44:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf61b855-150f-3092-81f0-604e178ffc54 | -10.75 | -69.37653 | 2024-10-31 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8257da9-02ef-3fe6-9a55-fc0fbfcf6971 | -10.71349 | -69.45287 | 2024-10-31 05:44:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ba2655f-b26b-31f1-b7c0-2a2eba15e143 | -10.88349 | -69.74301 | 2024-10-31 05:44:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8456aa79-b77e-3b22-9880-84d137a4e7a1 | -8.07118 | -70.88444 | 2024-10-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36ba07d9-76b4-3e13-aa67-559fdd6993c9 | -8.06711 | -70.88375 | 2024-10-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08d59ed2-c38d-3550-aec1-61536f1875ff | -8.03278 | -71.32555 | 2024-10-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e573a717-fcea-33f0-99e4-803ed48f6c83 | -7.98064 | -71.50415 | 2024-10-31 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5388d755-c7a0-3b23-aa56-db68df945ac7 | -7.02815 | -71.79304 | 2024-10-31 05:44:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e53880dd-d6ac-3443-8600-27ceae5c3b53 | -7.02742 | -71.79733 | 2024-10-31 05:44:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 790859d6-f766-3f78-a728-61dc183b372a | -6.90265 | -71.51339 | 2024-10-31 05:44:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9326084-df2d-363c-b255-fbea7d20a599 | -2.5409 | -54.0788 | 2024-10-31 05:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 6434811a-c7a8-3852-9888-da9af43db8f5 | -3.1094 | -45.2293 | 2024-10-31 05:45:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 2a7a6afb-654e-3d84-9723-51d98ac1af46 | -3.2209 | -45.2475 | 2024-10-31 05:45:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 1939609d-95d8-3243-b4d6-bff07e17a387 | -3.221 | -45.2249 | 2024-10-31 05:45:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e1c8e543-f9f0-37a6-a670-ab8217a8c87b | -3.2535 | -50.3479 | 2024-10-31 05:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 1ccde201-428a-3d10-a110-f9a9d80725fc | -3.2535 | -50.3269 | 2024-10-31 05:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 8cbe3b7e-241e-31e2-b527-3e83a7e69f82 | -4.8178 | -45.8429 | 2024-10-31 05:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ac3171a8-22ff-3aa4-8435-c1fa1288e948 | -16.97137 | -54.81741 | 2024-10-31 05:46:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10cce7dc-1ec9-308e-a254-a044349d2dc9 | -16.55448 | -56.23478 | 2024-10-31 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 15d11573-c982-37c1-bec7-a911d03adefb | -16.55401 | -56.23945 | 2024-10-31 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0a6512d2-ad00-3ecb-bf97-a5d3297e1641 | -16.56517 | -56.25015 | 2024-10-31 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e49810fd-d553-3330-9312-57e6f2824164 | -16.56052 | -56.23547 | 2024-10-31 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9ec11603-86c9-3e17-a012-2447278ac6b2 | -16.55913 | -56.24945 | 2024-10-31 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b0759034-1ad3-30b0-a1b0-fdb35a5c90b1 | -19.48066 | -56.61997 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 96e7407f-5e6b-3acd-ad26-40668da4c5e3 | -19.47634 | -56.66833 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7d79cf57-3941-3dce-9046-a3bf162bcb86 | -19.47457 | -56.61928 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 12a59124-301f-3cb6-9de9-1d707b2e9719 | -19.47241 | -56.6435 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e951a778-f373-365c-94ed-1c508ad4cd5a | -19.47198 | -56.64833 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5aca2ba7-34d9-3007-8721-cd951fd7847a | -19.47155 | -56.65315 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c5fa59be-c2ce-34e4-ad06-95abe0725d72 | -19.46847 | -56.61859 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 83315cb6-deb3-3d16-af6e-2c76f69f5f06 | -19.46756 | -56.61871 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6c0f720b-d36d-39e6-963c-7eb955890436 | -19.46589 | -56.64761 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 33d2f3a2-9e90-3625-a3f2-b130671976c8 | -19.46547 | -56.65244 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6766f389-54b7-308a-86e6-045083d12834 | -19.46479 | -56.64766 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 73007669-e48c-3ff3-976d-436093e34050 | -18.26216 | -55.96523 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6012350d-cf99-3ae3-a2b3-a6707838a595 | -18.26154 | -55.99183 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 604531e5-b5d7-334c-83f7-93b71811423c | -18.25984 | -55.99097 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 179eb8ba-eccf-31a5-bc36-c813969efc74 | -18.25827 | -55.9603 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 332d0ebb-2f9b-3722-8d35-ab3c9ef203c9 | -18.25778 | -55.96543 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 83f4ecd9-02ff-3361-ba1b-8bd6569cd46a | -18.25636 | -55.95937 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 60d0fa6c-2e83-36bc-adc5-ad13e1584096 | -18.2559 | -55.96452 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8ea61659-58cf-362e-8ad9-b8934b493d61 | -18.25529 | -55.9911 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fe754811-0fa5-38a4-ab58-40863c62ec92 | -18.25152 | -55.96475 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e36c94b2-1f14-3392-bf12-3cbf152857c8 | -18.25102 | -55.96988 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0e4eb5a0-45da-32ea-bb10-30c11b62878c | -18.24918 | -55.96895 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0c9c109f-4c91-34c4-a874-b12dcdf235f8 | -19.60359 | -56.69766 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 33ddf22f-bb3d-3ad3-a797-f7fd911ef83d | -19.60315 | -56.70249 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 855f7f09-5c50-3dd1-86fb-f6a25a67d794 | -19.60272 | -56.7073 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7375c4ab-e4e1-3473-9c88-83e56ee953d8 | -19.60228 | -56.7121 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 70cf6141-6bf7-3afc-9321-057601df65d4 | -19.60184 | -56.7169 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 805752af-b976-3027-8dae-fed2d7beb9c1 | -19.59665 | -56.7066 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 13ac26c6-ddcd-3f20-9b51-43d5bd75b738 | -19.59621 | -56.7114 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| a0a914a9-622b-3505-9ccd-cfc0198de764 | -19.59578 | -56.71621 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 189703bf-d343-3ad8-8524-73c0e084260e | -19.59229 | -56.61824 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d7b2bf76-255e-3fd0-94e6-c8ef22665678 | -19.59185 | -56.6231 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6b8a876b-5664-3f5e-9cc9-8cb7e6c61ab0 | -19.59057 | -56.70593 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 74de46bc-3b08-3aa9-9b7c-81fd3757f6ea | -19.59014 | -56.71073 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 92fb083b-9007-31fb-8e37-826497229fa8 | -19.58971 | -56.71553 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| f37c5a83-921a-3c35-9b7c-70b492b31aea | -19.58618 | -56.61754 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 49950c48-0096-3051-90b7-a42c4973c690 | -19.58575 | -56.62241 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 49821388-84f1-39d4-8dc4-48a925958c05 | -19.5845 | -56.70525 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e503baa3-5676-3842-a43c-5b49d243108c | -19.58407 | -56.71005 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1d38fa56-ea5f-3580-83ad-b3e46e4b4dcc | -19.58364 | -56.71485 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8c51d826-52ae-3ea1-b106-4940f4e17956 | -19.58321 | -56.71964 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 0ce9140f-7526-3995-96c7-97c10debf7a5 | -19.57842 | -56.70457 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 390459b0-7976-3ee2-9027-211f67937cdb | -19.578 | -56.70936 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2d9b604e-86e3-3b7c-b8f0-3bb275b9347a | -19.57757 | -56.71416 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 403e3cd6-f741-30f8-89f4-bd6f3c1d6421 | -19.57278 | -56.69908 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 76335db6-efbe-3cfd-9ede-8aecbdd5a38e | -19.57236 | -56.70388 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8e7151cf-ed6c-3424-9588-f873c9783990 | -19.57193 | -56.70868 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| cab532fa-158f-307c-b766-4fe1ee600c4a | -19.5715 | -56.71347 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| ba7257ca-c42c-334b-9b3b-957e04d40130 | -19.56671 | -56.69839 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f08b122b-d5e1-37fa-a7e3-ec1f93e32c52 | -19.56628 | -56.70319 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 95a79bae-2d11-3023-afbc-64fa911985cb | -19.56586 | -56.708 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 0f69d0be-49a4-3e5d-99ab-b3b58d3c8a7a | -19.56569 | -56.69775 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e39dcdef-2ffe-3107-be16-78435e735ff6 | -19.56543 | -56.71279 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 41e75a80-f9c0-3187-a104-7f84a6b03afc | -19.56524 | -56.70255 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 4e10b316-765f-3b75-9451-f4a7185fcea4 | -19.565 | -56.71758 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| b9bdd26a-d0d0-3887-a1cf-7d2ec4a5812e | -19.56478 | -56.70735 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| b262f3e6-c051-32f8-81a1-3d6d1e21e990 | -19.56432 | -56.71214 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 029006f0-bd23-3820-abd4-6bb95be5a4d7 | -19.56387 | -56.71692 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| d6975752-73e4-3fd0-8eb5-29e0b535ea32 | -19.55936 | -56.71211 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 19fd8999-52df-3cb4-9460-96170ee020e7 | -19.49548 | -56.59222 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 51f72595-4703-35bb-aee4-e50fbc0c4341 | -19.49504 | -56.5971 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a6d49f10-0d65-3fe7-822c-b3a047cd0e15 | -19.49285 | -56.62139 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1f8497c7-afe4-35a6-8e45-57f0dcc141e1 | -19.49242 | -56.62622 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| af6bf092-245f-31cd-b58a-6d70a241305d | -19.49196 | -56.6992 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |


[Clique aqui para ver as próximas entradas](README49.md)
