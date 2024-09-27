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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 088595c6-dce2-3b5f-949c-5a675ff69cb9 | -8.89794 | -54.72859 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7cfa571b-9fb6-35ee-abce-861e144a139e | -8.71634 | -54.81234 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa69147f-3b69-30fc-9a84-6cde97469b1b | -8.7151 | -54.80344 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2b1e3c0e-5534-3bb7-8493-1644ae4a0ca0 | -8.69882 | -54.75138 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 29dc76ce-9d79-3724-926f-5c65e82c3a11 | -8.69618 | -54.79711 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9bca8a9c-7fe7-313c-9f99-03625f708b1c | -8.69494 | -54.78822 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2cb36e55-1d6a-39e4-88be-f3b5f7249135 | -8.53676 | -54.58738 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f0679e18-f168-3f7e-ae22-a77f8effc5b5 | -8.53427 | -54.56958 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f1ce3427-a521-31b5-9b4e-a929fec696a5 | -8.52916 | -54.59755 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f06e52c5-fe8e-370a-add6-714364dbbac7 | -8.44593 | -54.66087 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7e7d70e1-342e-3c45-b9aa-89c7cda5bea7 | -8.43073 | -54.68121 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9cf9d664-2557-39cf-bc29-950e54660635 | -8.42091 | -54.54652 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa93f2b8-c146-365f-9752-e0a5981d365e | -8.41677 | -54.71043 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b346cf9e-3da8-374d-aa9e-940d8d67dec9 | -8.61802 | -53.65609 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c589813e-3424-3e08-97b3-636ee0c411a5 | -8.6167 | -53.64692 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e8e64a28-7f6a-3113-adf1-228b59ea8e30 | -8.58426 | -53.35773 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7a30728c-802b-3316-8da6-3535c931102a | -8.58155 | -53.339 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8be09a44-0d84-3fe8-bf34-e1013dab12ad | -8.5725 | -53.34049 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 25394aae-2f93-3e75-bcc0-057c6cdec459 | -9.46537 | -53.58839 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8fed0ea-bf28-3f0a-a59d-971adc823445 | -8.6081 | -53.6545 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 83973f42-1252-39c4-869b-95a0181f4075 | -8.57385 | -53.34982 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 7f193733-1296-300d-b2d3-21115b1891bf | -9.17647 | -54.67891 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e6e162f2-bd9d-35c7-bb52-1b02df1c94ec | -9.17522 | -54.67001 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4783dd69-f051-3d95-a46b-9bb0e22b264a | -9.17026 | -54.63441 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8ea8a6d-1ca2-30e6-bdb6-050ba47694ec | -8.92817 | -54.75144 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae8b4942-d0aa-3f75-af2c-8c38d46b7e56 | -8.79981 | -54.68513 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d401978e-3a98-39ed-86ab-b049c8706388 | -8.70749 | -54.81362 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be93fd78-5d28-3227-a8c9-e25151b2cb0b | -8.70626 | -54.80472 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| d27057a5-e880-3806-9761-c68dd0952ac3 | -8.70502 | -54.79583 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 654713eb-0707-3b4a-bd60-4e7f10ed39cc | -8.68486 | -54.78061 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1bdc9aa-6c3d-3ca4-a294-b7c946466ec6 | -8.67871 | -54.81461 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e57a98d4-5fde-3216-a2bb-b9a5b853ec12 | -8.53552 | -54.57848 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a72de2ba-9991-3a12-b7b9-78619fbdf9f5 | -8.5304 | -54.60645 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5a0cf7bb-977b-3736-b10a-6999502f0983 | -8.52792 | -54.58866 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6813694a-8d38-36be-b134-f030f30cfafc | -8.52667 | -54.57976 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 50182c75-2ca3-3b44-9137-206bcf8d0e1e | -8.51506 | -54.69033 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85099d1f-c917-3b25-af91-6421777f3533 | -8.42561 | -54.70915 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a69bcdc1-7dd2-3d5b-84df-7fca9cb6c066 | -8.42437 | -54.70027 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 81ffccba-f624-337e-9842-f250e5742c7e | -8.42313 | -54.69138 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d3d83786-cec9-319a-9944-41b40a4e76fb | -8.41553 | -54.70155 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fb4ac71d-13c6-3bf3-97e6-99e5652b339b | -8.4006 | -54.59486 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc9726b1-be61-3268-abf0-d4185ee7f430 | -8.21779 | -54.66976 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04474e8f-360b-3246-be0f-dd276c2e4080 | -9.81571 | -54.10912 | 2024-09-27 01:24:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01fef7a9-bef3-3415-9afd-ffe4e829b345 | -9.81193 | -54.01809 | 2024-09-27 01:24:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 03964305-e8bb-331c-bda1-e478bdd5d636 | -9.59658 | -54.26003 | 2024-09-27 01:24:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 796af360-87d8-3f1c-8eaf-1b20f4e1d906 | -9.59532 | -54.25109 | 2024-09-27 01:24:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 290d5cef-f567-3b70-a0ac-dfe2cbbc68fc | -9.46392 | -54.56467 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b00746eb-6820-3031-8cf4-7c83b17c0895 | -9.66962 | -54.25222 | 2024-09-27 01:24:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc42ecc9-f842-3457-8db7-135ba99741d8 | -9.66081 | -53.53792 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 832a7433-df2d-3fac-bdff-efa761c4d581 | -9.6595 | -53.52874 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 65041e68-f449-3a52-8dcb-b52095aa4ad8 | -10.46706 | -53.83314 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 272f3d1f-c85f-35c0-a0b7-72a7ae173680 | -10.46685 | -54.21791 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 082d0871-2564-31c6-a552-b74eb8c0c44c | -10.41239 | -53.70288 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| eac94e7e-0245-3f1d-b55f-e0b0e47656c4 | -10.41111 | -53.69381 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 49efb605-c637-372e-b7be-83eed57e96d3 | -10.3764 | -53.77874 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bc051c77-9516-32e0-aa8e-1b3502b879da | -10.37512 | -53.7697 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9c830bb5-07c5-3f53-85c3-5472b729ed78 | -10.37005 | -53.79812 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 1cdd4c30-8412-3115-8b7f-0a3991bdfc54 | -10.36878 | -53.78909 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 1023b0a2-4ea6-3529-9cc9-0745f1006624 | -10.36751 | -53.78006 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 6db5313f-303d-3751-b5a4-b42f85cf3626 | -10.36117 | -53.79942 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c39191a9-7093-3a9f-83b5-f36c985715df | -10.35989 | -53.7904 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 6c2a4be1-2ec7-371c-bba0-ad17300c5d49 | -10.35862 | -53.78136 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 590d6ce3-a191-36c4-981f-22f535bbf75a | -10.35607 | -53.76329 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7b0e7fee-c22b-3738-bf79-d46783219198 | -10.34719 | -53.76461 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3daa39fe-9fe5-32fa-8d5d-a2e5b0bd0b8e | -10.23159 | -54.12431 | 2024-09-27 01:24:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 989c2b88-169b-3c93-9155-fd4c82b045cd | -10.22274 | -54.12561 | 2024-09-27 01:24:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9f7931cf-68dc-32eb-a122-8df5a03f565c | -10.20886 | -54.0911 | 2024-09-27 01:24:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48d5c50c-d397-305a-aca2-3ecaa28746b4 | -10.62248 | -54.60892 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1ce32083-2522-3bed-af59-0d6df0bd7dbe | -11.32612 | -54.04577 | 2024-09-27 01:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 47602c83-373a-3478-bd76-64aa8d969846 | -11.31727 | -54.04707 | 2024-09-27 01:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 63ac63ae-01b6-3306-8229-5778993665be | -11.31601 | -54.0381 | 2024-09-27 01:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7a0d174b-acaa-3144-a3fb-5b3a0df26548 | -11.21906 | -53.9395 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bc388af4-0420-37e7-a3bd-48877ff33b79 | -11.19757 | -53.91517 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 26e1ed7f-c49d-3f48-8554-ec0c2aa907ba | -11.19631 | -53.90617 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 8242a535-ac22-3a09-8b0b-983b6e5c6099 | -11.19504 | -53.89717 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0470f318-db1e-3657-86b8-f5ad7d45b141 | -11.18871 | -53.91648 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 99543a15-fc5f-3646-afda-4fffa180a1be | -11.18745 | -53.90748 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 57287a55-cb4a-376f-a68e-2e93ecf0e925 | -11.14334 | -54.1855 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 81e9104c-0a3f-3244-bc25-439d410e4fed | -11.14209 | -54.17653 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cf2395bb-d24c-3869-8067-6e65d3c5fdc9 | -11.13449 | -54.18679 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f578b66e-8fd6-33cf-b63d-ca286c07f83a | -11.13324 | -54.17783 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b7ef2c1c-0dcb-308d-a296-13b883408415 | -11.03388 | -53.99738 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 680dc661-03e3-32df-a2fe-298674c516d1 | -11.01747 | -53.94482 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| addd8217-6b25-30c1-8a66-fabc050bb806 | -11.01621 | -53.93584 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cf709635-26db-33ee-bc3e-7dc25f2e762b | -11.00735 | -53.93715 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e06cd39d-dccf-3f54-a5e9-9383b671c98d | -10.94417 | -54.27259 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b4cd864-3825-32a4-bfd2-62e8c99445c8 | -10.94292 | -54.26364 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 52c3b654-2dde-3e11-bc7a-114eae955a7c | -10.93532 | -54.27389 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3ea8fb36-9115-366d-9fe6-b0c704575bec | -10.93408 | -54.26493 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 8d9a5081-d6f5-3abf-864e-f95a7ffb3edc | -10.93283 | -54.25597 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 60b3ab96-f700-3b50-84e2-7a0cf0a8338f | -10.93158 | -54.24702 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0b40561f-87a8-33be-800d-1707b220aae4 | -10.92648 | -54.27518 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3afa7cbc-8c5d-3178-978d-57a8a7e8cc58 | -10.92523 | -54.26622 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 229.4 |
| 1b08537b-81de-3f40-9666-8f9a0691648f | -10.92398 | -54.25727 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 302.1 |
| fb80c521-38f4-36a7-b94c-7253492f2def | -10.92273 | -54.24831 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 12063c2f-a712-32cc-aa68-4546b419bdf4 | -9.62386 | -57.75972 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 042b0f5d-de02-3c55-a815-1f86d13662b3 | -11.67797 | -54.44651 | 2024-09-27 01:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 850c1f41-092a-3fa0-9f4c-9e48737defe2 | -11.67673 | -54.4375 | 2024-09-27 01:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bbafd91d-9482-3500-81ee-a78bbf8c286d | -11.66703 | -54.44526 | 2024-09-27 01:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b914d6de-258d-32da-901a-d663388d9792 | -11.22563 | -54.77893 | 2024-09-27 01:24:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |


[Clique aqui para ver as próximas entradas](README26.md)
