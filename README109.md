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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14a948fc-cdb2-32de-915b-acc766fee059 | -7.50614 | -54.99987 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 076b8df4-c848-31fa-8ab0-b6da316f01ae | -3.58142 | -55.6068 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4077d38-ebb2-3d9f-8c88-8ef66126b9ce | -2.90202 | -56.94799 | 2026-10-10 05:04:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5aff1ad-bf79-3f1d-8748-2a636a73f92f | -6.32804 | -58.30887 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be951294-852d-302d-b91b-873161e4271d | -5.87708 | -50.09916 | 2026-10-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 279f168b-4366-3ec3-8486-02d480693790 | 0.22451 | -60.3852 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9769d0b-8c6e-3c0c-9297-b97bbee70a6e | -3.60299 | -54.56599 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25de8d72-0200-3fd4-8ce9-8117c2ec2e83 | -5.23532 | -60.19048 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f01ae4e-914a-379e-aea7-ec0dd5148599 | -5.99223 | -55.37419 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81c58a04-07d2-3140-8637-16434979da64 | -8.23871 | -46.43125 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88d6524d-993f-35c5-9357-210337b3e749 | -3.18687 | -50.58891 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad1a5ce6-2e36-3308-8445-6a717070a939 | -3.07046 | -54.36782 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9977520-cd52-3ecb-8c38-75c2adc5ff22 | -5.60104 | -47.2871 | 2026-10-10 05:04:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2544118b-3e75-3d1d-877d-6e5fd239d5f7 | -6.32379 | -55.34004 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6153d7d-5800-37a1-ad15-7d42d07b0bca | -2.28717 | -48.75735 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 656d2cb4-a136-3f2e-ab70-9475e8532ff0 | -5.78944 | -53.80469 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1764a94-2d4f-3b2f-badc-241bfd358819 | -5.62391 | -43.64859 | 2026-10-10 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eac42e34-5ecb-3766-b0c6-70d2a0b740cc | -2.49364 | -56.19055 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1272f22f-aaf4-30db-b198-3f2459fab7f8 | -3.01978 | -54.04432 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eff7ecd-8e46-3478-9ec3-8b56878a6877 | -3.30797 | -53.70515 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d865862-5117-3104-8544-f43824467ccd | -6.18822 | -55.97158 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c85acc11-f253-3590-b088-d8b334d56b63 | -3.03335 | -53.89465 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a9b2774-361d-3b1b-ab90-d8d12327c824 | -2.39063 | -51.30361 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f622248a-b8e7-31f3-9914-1a55384b791a | -7.24473 | -55.21093 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c2d675-2b17-3544-ac78-e25cd672d475 | -3.26923 | -54.25014 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8194aee-4dfa-3f6e-8a03-d7cfacd90710 | -6.41718 | -55.28674 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a84fc2f1-85a2-3af6-af99-a69675eb4c47 | -1.36619 | -56.93116 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9dee006-9cda-38ed-a467-ec4bd59ba803 | -3.56522 | -54.6962 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8fb9e3f-aad5-3917-87e8-4ee5633eff13 | -2.97792 | -54.11555 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd23580d-8832-3fa3-a412-7da5764ad341 | -5.87777 | -50.09453 | 2026-10-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 593e4f36-4d79-3f24-b648-32a8944c61bc | -2.83773 | -54.14301 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e44da880-a4ea-3e0f-aa73-3dee85da1223 | -6.75211 | -52.94685 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76910c53-0c0b-36fe-bed2-fc854ca96776 | -2.48202 | -56.17247 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3a118c6-dbb6-3c52-9b1e-40cb1a2efcc7 | -4.24301 | -56.30875 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a682c43d-a5fb-3e26-9422-21713ad7e8e0 | -3.31975 | -59.84371 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c92470-feec-3979-9c2f-e868de2db61f | -1.26462 | -55.74789 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa5a43d-e334-3c3e-b868-b40f02ff5e9f | -1.33127 | -56.39568 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f91a9c6-046d-3865-8293-76da0179b092 | -5.96905 | -53.54784 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf7d9630-08e6-34d7-94cf-b9cd1c4fea66 | -4.1222 | -46.86623 | 2026-10-10 05:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 25e8fada-05d1-3aac-b8cc-fc12a7015523 | -3.09497 | -53.93586 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 679469b9-ad40-3007-a3c4-439820a98962 | -3.18922 | -58.65836 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a195e557-95f3-3fb5-b144-e719e89cc9b4 | -3.11011 | -54.1609 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01357892-f7fc-3c4c-9fa9-d323ce74e04e | -4.12101 | -54.04214 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afdc2c18-8126-395e-bd53-fc4782084840 | -3.16317 | -54.72651 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e13ef1fc-5d2b-35ac-b20d-cf498886d6db | -4.14077 | -54.00293 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 314fcc3c-da05-3452-a1d6-801f045a1270 | -7.23738 | -44.18317 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c073d618-3fcc-30ef-8e65-aede7c761c3a | -6.46066 | -55.05692 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e04f2260-0703-39ca-8cf4-9233299ed037 | -3.12449 | -54.17733 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8ef5dd89-485a-3ede-b538-c8190e76bf22 | -2.94148 | -54.10981 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e68bf082-3788-395e-aa74-2584d80543be | -6.15217 | -53.31092 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e614c644-043f-3644-a8f8-0e7baae408cc | -3.31244 | -53.87185 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c5c2787-ab24-3239-95a7-258cc3483bdf | -5.99557 | -55.37475 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cadfc49a-eaab-37fa-84b0-70b0fd5eba02 | -7.18513 | -52.63715 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 881728a5-06b7-30bc-bdd1-b9cd23f0cada | -3.53113 | -59.57503 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a967b167-315d-338b-948b-da84a699b716 | -3.95732 | -60.00408 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef46b10a-b750-3696-bc68-c605fa959c17 | -5.86844 | -53.51754 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51f5e19d-2ee7-3cd0-a102-65f8e69f482e | -5.18004 | -60.305 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51b64533-c39e-3fc5-8c90-eb76a2c14a81 | -3.35129 | -50.41727 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1deb628-e574-3543-b1f8-9298ca0a6758 | -3.39486 | -58.00143 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 137b3085-36e0-3e47-97a0-cd744723368e | -6.0621 | -44.65729 | 2026-10-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e852a1d3-e9e7-3e29-9484-b9f0f204a9b0 | -8.24846 | -46.43536 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b04d3fa-b39d-3e93-9240-6c7e5a54d514 | -2.99864 | -53.89978 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62dcb667-04c9-355d-8d6e-42b5e8506ea5 | -3.37516 | -59.38918 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24c16b15-b25b-3fe7-b432-eba12c7732b8 | -7.2127 | -55.15611 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84a53786-fad4-31fc-bcae-f404df071e39 | -2.85984 | -54.17485 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 804971b7-e971-3431-888b-25733bf1660f | -6.06155 | -44.66109 | 2026-10-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da9eb2d8-3478-3e09-a872-eec569d52242 | -3.92724 | -54.57867 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5486a292-e2e9-3d01-a13b-895b617b7ee9 | -3.51501 | -58.02781 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9eed672-b238-321a-b6b2-217fbef7d8e7 | -1.45044 | -54.4715 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac12e092-d428-32d0-bba8-e78f93c84094 | -6.47504 | -55.07352 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2f2284c4-bb9d-3ed6-b42e-a46a65428aa8 | -3.05498 | -54.76001 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20ab0a46-d566-3b78-9131-6e507429004c | -3.22561 | -54.2891 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1cdda7c1-2260-3beb-8e79-627673e675be | -2.21829 | -53.69849 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff6a65ee-bb50-3fef-a430-a951c701adb4 | -5.36765 | -60.10216 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a85352a-aace-34cb-92e4-07a9c0ceb5b2 | -6.64473 | -55.33068 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec6d9ca3-3558-34bc-bf42-d9c3d92ec0a7 | -3.30688 | -53.71203 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e11a26a9-6214-345e-853b-218173039ee2 | -3.95209 | -55.3326 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d5541d1-5efb-3ec0-ac6b-6fd1209af1ff | -5.79221 | -53.80867 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6af7461a-44ce-358c-914d-0f786f433be1 | -2.9857 | -54.17349 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3095965-8a9e-3385-a0fa-f17b967e3672 | -5.22459 | -60.04634 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c51942df-91dc-3efc-873c-4a0d81cbd4df | -3.2037 | -57.86794 | 2026-10-10 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83348389-426a-378e-b556-42c5fc2c0dcf | -3.39566 | -57.99665 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aab51127-e1df-3ff7-8cdb-68f1374c7b51 | -8.23403 | -46.42778 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8389660d-ff5d-30ac-9196-106134471993 | -0.87764 | -48.71545 | 2026-10-10 05:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32c1811b-d75f-30a6-aec3-126306077537 | -4.90276 | -54.98061 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32aaa881-12e1-3ff0-9427-c9d7c3b8749e | -4.58685 | -54.93695 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de9aad0f-3e6f-3766-94f2-03360095317f | -2.73162 | -54.14722 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9364d2f9-1908-3aa7-9232-07b58fdd05f0 | -1.95636 | -54.40706 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c67d628c-20db-31d3-9a0a-3637dc85cbbd | -3.25452 | -54.02099 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c80d42d-cdd9-358a-860c-746b43104c40 | -1.24075 | -48.11686 | 2026-10-10 05:04:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7365417-a94b-3a2e-9de8-292c6fc49915 | -3.07817 | -54.27645 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50f09107-cb37-30aa-8afa-c970bbfc2ea7 | -3.03799 | -50.3395 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f082555-6353-3505-9d7c-b6c9d65c0f24 | -3.24091 | -54.66339 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb2b9cf7-e4ec-3ff1-a706-114c04d5ae4c | -6.70671 | -49.13154 | 2026-10-10 05:04:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4777120c-e1ba-333c-9a62-fa146f0dfb6d | -3.22065 | -54.29897 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf9bb332-2935-315d-b766-c04d97a8caa9 | -2.99588 | -53.89581 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c49af0f9-dbdf-3caa-a10d-620465ce1645 | -4.36423 | -55.64684 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e6c4ae4-531b-35f2-82cf-31578b81561b | -2.63079 | -56.46572 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81618b13-b10a-33b7-b7dd-f6a71a2f64fc | -5.95266 | -45.38388 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7164dce6-39d9-3268-923a-6ba0122932bd | -1.26525 | -55.74399 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README110.md)
