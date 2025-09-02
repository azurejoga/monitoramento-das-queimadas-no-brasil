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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1154cae6-7b42-3deb-b1a0-bcb81adefbc4 | -6.80939 | -52.81773 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 784d69f3-74c2-3934-9859-22ba0e9c20fe | -4.58123 | -48.01893 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd464f8-65df-35e7-9242-8beccab9fec8 | -6.30667 | -57.97922 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02741f67-08ed-3712-9215-f75e200f2821 | -7.70961 | -45.01801 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6aefbcc-a83d-39a4-8b65-05aaf41dd8ee | -7.76829 | -49.48469 | 2025-09-02 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 886d1bb9-be0f-37e5-8dc5-8ebe6542d4a1 | -3.7314 | -49.68254 | 2025-09-02 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb78cd34-cb03-3b4a-9e59-fd70129c2740 | -6.21913 | -43.36185 | 2025-09-02 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f9f4bf3-9dca-3ef3-87aa-4f1385257b30 | -5.69948 | -45.95094 | 2025-09-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 805f4950-aeb3-3c7a-a7b1-b4184dc7991a | -7.87561 | -47.96727 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac8e6262-2a88-3b60-9fe0-61938dac8990 | -7.38168 | -47.04571 | 2025-09-02 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cafb90f3-9773-393a-b161-0b3ea22548f5 | -5.34751 | -55.87612 | 2025-09-02 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0bc4f092-9cff-33d1-b974-2a59fda59e2e | -7.49804 | -45.35067 | 2025-09-02 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b95d9fe6-67e7-36fb-aab7-a093924021b0 | -6.54184 | -56.19975 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdf8900f-35ae-3dff-97dd-3b4f5f4aeb49 | -7.70417 | -50.28218 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a1a9763-2945-385c-b49f-c791b7bbc124 | -7.92257 | -46.44745 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dc90b03-0603-333e-962f-0a137b44d1df | -7.37876 | -48.19474 | 2025-09-02 05:04:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65f80534-a90d-3ba6-ad81-e9a22cfa5d60 | -6.85893 | -52.80811 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49b4eb2c-4261-3551-979d-7cfb680c5b87 | -7.27951 | -60.64621 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0ed3dee-6ff6-3db2-9159-d81839ffa417 | -6.8366 | -52.8089 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1be52906-f05c-34f0-be3c-37bc46588e2c | -7.69248 | -50.27212 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d765ddd1-21c3-3277-8131-8dd2e1ec1aaf | -6.85403 | -52.81595 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 179ad0da-f122-3de6-a53f-438147e943d2 | -6.82857 | -52.83758 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 317e3b64-609f-3431-a22c-9cf364232f05 | -8.3476 | -52.53035 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adb2fd60-b7ee-3146-be39-db132313bb93 | -8.7091 | -50.4359 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1de8c165-73e7-37a4-838f-35516094698a | -6.79131 | -52.81495 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 217f6092-3e5f-3cfc-bcd1-8151e06148b1 | -2.3427 | -47.5864 | 2025-09-02 05:04:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cda2204-75cd-3650-a684-b8401c18cb13 | -2.90861 | -48.29693 | 2025-09-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1658bcda-e371-3b50-8939-446e2fbf35f5 | -7.98296 | -46.45369 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd9ecad0-efba-3bd9-af73-a046d409a03a | -5.11675 | -43.23064 | 2025-09-02 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f74d5216-eda5-3df5-bb85-e00e41bc9785 | -6.78769 | -52.81444 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4a91b83-91bb-3729-8571-9bcef7b0ec83 | -7.70649 | -50.26569 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 21eed0ff-328d-3210-9142-bfe569843f7a | -7.57554 | -45.22488 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14129c48-41e9-35ac-a8c4-af2a56d9aa79 | -6.85637 | -52.82489 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7cfd7a1-cf02-3397-a756-f0445aa8bb72 | -2.88273 | -59.22639 | 2025-09-02 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2793d314-8233-3067-8f71-220d5eebc43f | -8.72033 | -50.45003 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 16835e3c-d7ac-30d4-9a57-a2eb63b4a6d2 | -2.65849 | -48.79647 | 2025-09-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 693f3bcb-f044-3f48-8c42-86da3cce8540 | -5.85319 | -43.00601 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 10ab4dd9-15e1-35e3-87ed-c6d100455abf | -5.858 | -48.15942 | 2025-09-02 05:04:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9825d083-130d-3856-b4de-85e297326fb3 | -4.22641 | -47.21398 | 2025-09-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5960eb20-d1b7-36ee-91fc-0425ef65b73a | -6.79556 | -52.81128 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f46c6187-bff5-362a-b30a-46b2c5c6d5a4 | -7.78331 | -45.44582 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 610db8e1-5f73-3c5a-8ad1-2cd6dd88e69a | -2.74926 | -48.67164 | 2025-09-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cc20987-2989-3f63-b175-f8b74b50cf8e | -7.70047 | -50.27743 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 775aa6f8-8473-3d99-9fee-56386b3c4adc | -6.77262 | -52.81639 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92fbe424-440c-32c7-bc5d-c4d3461fa2da | -4.92226 | -43.20052 | 2025-09-02 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49f2bc35-730e-3a04-a3e8-ebe7f69b9ca2 | -8.46368 | -47.36454 | 2025-09-02 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d90526f2-fed3-3543-a2c6-7cc54ff21000 | -6.76057 | -56.39066 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9def0a2a-d3d6-3108-adda-06695b24f792 | -6.35001 | -55.55756 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87f98566-e14c-3f77-b286-f4e5c7193028 | -7.63791 | -46.55726 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8a28a36-d2ff-3b50-8c6e-db8ea5a7b86d | -7.54977 | -45.72749 | 2025-09-02 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5123c8a9-2099-34b9-a3c6-bf5e3963bbc5 | -6.96396 | -44.35337 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed7a59f7-7d01-3805-8da3-2c8169224c12 | -8.00898 | -44.04821 | 2025-09-02 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73e80854-c9d7-35e0-a4ad-b383aab3f93a | -6.53031 | -56.20856 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ead42b4-dde7-325a-952d-98660d6f34cc | -6.80639 | -52.81302 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eebbbe73-531d-3d20-98e1-2b2fc69f27d5 | -6.83281 | -52.83398 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e502c46d-55f6-3351-8260-1b15be9c641f | -6.874 | -45.85302 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c020651-bfd4-3ffd-ad78-c650ce7c14dc | -6.83321 | -59.67941 | 2025-09-02 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a311787-5c52-30dd-a9ca-dd7cab668794 | -7.87058 | -47.96653 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5574718-c568-3f51-9f1d-23a757801441 | -8.86087 | -45.79509 | 2025-09-02 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| db4b97cc-0664-3613-a20f-457bdab32180 | -7.31084 | -44.28157 | 2025-09-02 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 109988ce-5cb7-3672-84a4-4cd564c839b1 | -6.85531 | -52.80756 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ab5266e-17fe-3132-8c32-76faf9183533 | -6.87343 | -45.85716 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8d2a2a7-3ce6-3bcc-aa83-b0a43607bdf1 | -6.81724 | -52.81464 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ef8749a-fbce-33bf-831b-fafc178d10b4 | -7.87592 | -47.9675 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10b7c898-9023-36df-b21c-19bd93c3f6df | -6.83298 | -52.80836 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 648945f4-a9cb-3279-8a9b-0e2f6e1251e6 | -7.99134 | -46.47662 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 814eaad3-5355-3194-8356-66e1d9b27e64 | -6.34804 | -53.43192 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 482c2912-27c2-3112-9e06-8345e061fa12 | -6.85721 | -52.79509 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9788bd79-101f-355d-92eb-5d7942ae7c63 | -4.91567 | -43.19962 | 2025-09-02 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c414a8e7-29da-3372-a4b5-9afaedf88ddf | -7.28401 | -60.66701 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8b2e4f4-4cd1-3dc4-8e96-a38891581d08 | -6.86206 | -52.81971 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c24d894-1835-304d-99d1-424fab661a4a | -5.69897 | -45.95471 | 2025-09-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e93e02f-d04c-389c-91cb-9fd2420179cd | -7.70165 | -50.26906 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a2adb7da-cd06-32c5-a8fa-594fb53a4d72 | -8.36259 | -52.53245 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf5aa3fe-ba32-3a6d-9f48-6a4e3429ab72 | -2.44568 | -49.36739 | 2025-09-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82bc7d10-33df-3070-9048-e54a86f94cd9 | -7.78092 | -45.44605 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d37e362-11b9-3090-b3b7-d72a10014c4a | -5.78764 | -42.58664 | 2025-09-02 05:04:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 698bfc27-e3a5-37b0-8a34-1585fe417d25 | -9.26345 | -47.12081 | 2025-09-02 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71eac8e5-54c4-357b-b1f8-3ff7302f88ed | -7.34684 | -57.62765 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2271b39-313b-369e-a321-cfab179ed82c | -3.44818 | -49.49543 | 2025-09-02 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2269c38-6bac-3eb7-bd33-cf32bfcbbbef | -6.77623 | -52.81696 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b28080d9-bbce-3a4f-9f79-e445bf98eb03 | -7.6102 | -46.03661 | 2025-09-02 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 47066129-ee87-3d03-8295-7cecfad074b9 | -6.83172 | -52.81673 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5863d45c-4a98-3cd1-b82c-e8c3148253d2 | -6.98507 | -44.31495 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b32ae8ef-54f3-39fc-8ee9-cd7891c36769 | -6.86276 | -52.78976 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a0db403-1314-3836-a6b9-5f13e51e40e8 | -8.12687 | -45.03201 | 2025-09-02 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5ea0125-510c-36fb-a52c-5b6ec798695a | -8.87543 | -45.77522 | 2025-09-02 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22d61d7f-5902-3c3a-a4ea-d6a9f51fc90c | -8.85102 | -47.55077 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d4c8db0-9d37-3aa3-ae93-cec3360461af | -6.40082 | -58.20279 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3467a005-7bab-3b7b-b198-bc684bbc42b3 | -6.85106 | -52.81116 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4c94f33-0e22-37bb-8ee5-967199f5924a | -7.3151 | -44.27792 | 2025-09-02 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56e03056-13a0-395d-a2f5-5c2c7d76f33c | -7.54923 | -45.73164 | 2025-09-02 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02db360f-a454-3cb6-b0e9-466314ccddb1 | -7.69677 | -50.27267 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b3683aaa-d9b9-3995-b8bd-ab05a01ff4ec | -8.85557 | -45.78959 | 2025-09-02 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e85a2adf-9f17-315d-b816-e0a06d705941 | -2.44476 | -47.33076 | 2025-09-02 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22b4451d-d23f-3af5-8309-b9ea9ad83926 | -7.85557 | -46.74083 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad8721e9-40d9-33e2-a514-acd7a26b5009 | -6.85295 | -52.79871 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efed4910-cdf3-3037-8401-02e41f145caf | -7.25765 | -57.54722 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0fe2045-0017-3c26-b4a1-157d6df30640 | -7.72177 | -50.25047 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f766106e-1906-3689-8d8e-3021853abefb | -6.19682 | -53.76247 | 2025-09-02 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
