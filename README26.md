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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe742b1b-f076-33e2-a10a-e97aaf7cb284 | -16.90895 | -55.79749 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 132.1 |
| cad76c8a-17d7-3fa1-9237-d906465cb193 | -16.90717 | -55.7817 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 1d01e292-c5f4-3379-ac41-b396d78c15c1 | -16.8996 | -55.80507 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 153.7 |
| 20215451-0281-3705-b1c4-a77d31954712 | -16.8993 | -55.81485 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 9a3c24a1-d4bb-358d-8b98-03f95485a3fe | -16.89771 | -55.78925 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 167.6 |
| 27a8436f-f256-3a69-9843-7bf554f5c450 | -16.89752 | -55.79893 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 187.6 |
| 3d492fb8-69be-38ea-bfc9-84c8b07e7e53 | -16.89583 | -55.7735 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 533a011e-f864-36f3-8ad5-6fdfdfb5c4e8 | -16.89576 | -55.78312 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| b970386a-00c9-3833-a788-f5768bd14629 | -16.8957 | -55.87025 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e8b8cad2-cf45-3d87-ba8e-010b9e4660d6 | -16.89005 | -55.8224 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| c9359bea-fa04-35dd-8497-5e0b06146cd0 | -16.88817 | -55.80653 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 277e6599-060c-3c5a-a819-cf8130bfa903 | -16.8863 | -55.79071 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 34.7 |
| ec6214ca-55fb-36e2-add8-dbb4e01956aa | -16.87994 | -56.73467 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| ea36c039-ab69-3096-b864-fff0e1f6bdb2 | -16.87785 | -56.7161 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.5 |
| 20f97a54-9601-3dc7-b078-1fd31362c102 | -16.84305 | -56.73915 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| b87ec444-fa25-3ac2-b909-4e4064ed9cba | -16.83979 | -56.74601 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| daa19623-5a4c-3fce-a4d8-b6c893d082cf | -16.83899 | -56.70203 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| b5ef50dd-8ec2-3f37-93bc-2ee72656741c | -16.83762 | -56.72744 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 14075dd9-094b-3027-a348-b1bef02b1fe0 | -16.7721 | -56.69785 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 5662cb31-cbf2-38de-8e3f-71009a9687e5 | -16.74964 | -56.71931 | 2024-10-09 01:11:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| ac1e3dc2-99d4-3318-adf0-2dbd27273d0a | -16.64626 | -55.89721 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| a463e3d2-5bda-3d9b-b3c7-cf21cb35cfc7 | -16.59817 | -55.57854 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 020fae3e-7237-3d3b-8736-509e0e8bf64a | -16.59808 | -55.57278 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| f794f700-a0cf-36f6-a11a-374df2471898 | -16.56843 | -55.91276 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| bb25766c-c151-3442-8644-0527bc6b13b3 | -16.56321 | -58.25607 | 2024-10-09 01:11:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| ca96f2d0-2190-3e69-8c87-ffddb9265064 | -16.53257 | -52.87663 | 2024-10-09 01:11:00 | TERRA_M-M | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2a526118-3236-3de8-9e03-5fdeb5168b2c | -16.52324 | -52.87799 | 2024-10-09 01:11:00 | TERRA_M-M | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9f347f1-ff72-3940-8e78-cc2dffc1a5ef | -16.50456 | -52.88073 | 2024-10-09 01:11:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 9f90c157-5486-311f-8f6e-70279f25a664 | -16.50323 | -52.87046 | 2024-10-09 01:11:00 | TERRA_M-M | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 07880e75-778b-353c-9260-b48f17bac3cc | -16.42609 | -55.95893 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 120755ac-8728-3c88-a257-1ed2c8b7e344 | -16.42422 | -55.94294 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| e12eac21-b7be-386c-9ae8-57259a857d5d | -16.42236 | -55.92704 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| 70916db3-e4d5-31e5-a63a-3045bbdfb2cd | -16.41275 | -55.9444 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| b4abb125-b6d4-3d06-afbd-8437849a7803 | -16.41091 | -55.92846 | 2024-10-09 01:11:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| d66fde80-4dc7-3f52-af87-4b3ae8290235 | -16.12811 | -55.85479 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 9aeeb5f5-9601-38de-ae24-95b5f5327d43 | -15.92671 | -55.02082 | 2024-10-09 01:11:00 | TERRA_M-M | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0e5e2e69-41c1-39ab-8a45-ad703492b9f0 | -15.92515 | -55.00783 | 2024-10-09 01:11:00 | TERRA_M-M | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 55278209-927b-3156-a838-ea546ef3aa62 | -15.69787 | -59.39146 | 2024-10-09 01:11:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| f89b26b0-4209-3821-b8d1-4f503a04524b | -15.65664 | -59.43158 | 2024-10-09 01:11:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| b3b68233-f5fe-3a14-ac09-b0cb2fc6c415 | -15.656 | -59.42467 | 2024-10-09 01:11:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| a1e48f71-b363-367f-8226-055ac528b0a5 | -15.52517 | -59.61119 | 2024-10-09 01:11:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| c7b50296-6190-3d19-8d4b-6fb71d47e37b | -15.5234 | -59.60467 | 2024-10-09 01:11:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ba7e0b3f-42b3-3c65-b73d-c24520b0e025 | -14.77711 | -55.9303 | 2024-10-09 01:11:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 94e76125-845d-3731-aac4-2b9b33ccb93e | -14.10233 | -51.09932 | 2024-10-09 01:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b659b1bc-b3a4-3936-9a4a-406aa428b882 | -20.75602 | -48.52869 | 2024-10-09 01:11:00 | TERRA_M-M | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 36a1c324-c897-3556-bef9-38d113f63a40 | -21.29547 | -47.21848 | 2024-10-09 01:11:00 | TERRA_M-M | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9bfcdebd-273d-35d4-813f-c4506a51a32a | -21.1142 | -47.24033 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 24506b5c-913a-3dba-b748-4ff86e709e9e | -21.11256 | -47.22979 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 73fca0ac-adaa-3b5c-a81c-415e8344260b | -21.10479 | -47.2422 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 77e47326-4a0e-3508-a26c-8873f1cd6845 | -21.10319 | -47.23195 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 460e50c5-8dce-30f8-bbb9-1b67f5101f64 | -21.09371 | -47.23345 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 31.2 |
| d85d5ad6-0ada-3e7d-887a-0922f9312d1b | -21.09203 | -47.22274 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e60bfab0-0632-3acd-9778-8136a729554a | -21.08814 | -47.22978 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 99fad554-cb1e-302c-9da5-7f1f826d7f0e | -21.0865 | -47.21906 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 43bb66c8-7b99-36d8-baca-09d12837e41e | -21.08478 | -47.20769 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5730f8b4-e8bd-3c42-82f0-543bfa34f490 | -21.08398 | -47.5805 | 2024-10-09 01:11:00 | TERRA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0e51cfcf-d0e6-39d1-816f-d290386a347e | -21.08236 | -47.5699 | 2024-10-09 01:11:00 | TERRA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e59da000-bc59-3469-bbea-baf3d071ea95 | -21.07701 | -47.2205 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0d4064c4-8e9a-3f95-adea-6c40cdc55715 | -21.07304 | -47.57147 | 2024-10-09 01:11:00 | TERRA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fa9c63df-10d9-307e-af79-21f946062d66 | -21.07143 | -47.56097 | 2024-10-09 01:11:00 | TERRA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba0f2cea-4269-3d93-a801-fc6ef46a94e8 | -21.03076 | -47.58555 | 2024-10-09 01:11:00 | TERRA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ccd4c356-d6a5-3a67-a71b-ab96b187b93d | -21.02914 | -47.57483 | 2024-10-09 01:11:00 | TERRA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 9889ee67-2ae2-39e5-880d-7118c9a5d4f0 | -21.02146 | -47.58723 | 2024-10-09 01:11:00 | TERRA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 285db772-1b56-3be4-9d78-7739040925d8 | -21.01985 | -47.57666 | 2024-10-09 01:11:00 | TERRA_M-M | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a0a0765-7957-384a-81af-47229d454084 | -21.00502 | -46.10096 | 2024-10-09 01:11:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| ece793ae-e437-3259-a57b-05bbe7552c52 | -21.00302 | -46.08838 | 2024-10-09 01:11:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 5812998a-34e3-37bb-a370-6e990fa27263 | -21.00281 | -46.09566 | 2024-10-09 01:11:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| e5e08c31-fcb1-3dfb-8825-592449c26602 | -20.98926 | -47.15733 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 938226bb-a5d1-3ba5-afe4-4ecb3e7eb3db | -20.9859 | -47.16377 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 289cf21b-e2db-37e3-8c5f-5d99be049757 | -20.98426 | -47.15314 | 2024-10-09 01:11:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28b02780-7920-3414-8ff2-72e59e733b92 | -20.87315 | -49.20886 | 2024-10-09 01:11:00 | TERRA_M-M | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c77e9aa8-9445-3354-a6d2-c49aede64125 | -20.80039 | -47.22139 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1b9d987c-841f-32af-bd18-f25dd7ebbb3d | -20.79868 | -47.21013 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 7557defe-c845-3c3c-a5b4-f1fbc92ac2fa | -20.79697 | -47.19899 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 41db9f46-4b1a-3a93-b975-4e7573850cd4 | -20.79258 | -47.23402 | 2024-10-09 01:11:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4969ed36-12d3-37e3-9229-4566065e45ec | -20.79087 | -47.22287 | 2024-10-09 01:11:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ca4d8f09-a8c1-39d6-8339-5742ea44e5d6 | -20.7892 | -47.21201 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| ce9f56d9-4bb9-391c-935b-0af8cc9e6056 | -20.78638 | -47.25695 | 2024-10-09 01:11:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 5014ba68-6c32-30c1-a9b1-389c2442df1b | -20.78474 | -47.24636 | 2024-10-09 01:11:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 0ec66090-574a-3b27-a6b7-55fcfbd66a2a | -20.77966 | -47.21335 | 2024-10-09 01:11:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6a3c885f-3084-330f-a757-df8ef91094d8 | -20.77835 | -48.55487 | 2024-10-09 01:11:00 | TERRA_M-M | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b2b05cc9-b459-3b8a-87fd-065b0c5e45be | -20.77688 | -47.25849 | 2024-10-09 01:11:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 4dd681e7-9b75-3335-bc04-ec96fe00c0f6 | -20.77519 | -47.24755 | 2024-10-09 01:11:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 96.5 |
| c09617cb-b047-3f3b-8a51-100bc2f94c0b | -20.76323 | -48.57753 | 2024-10-09 01:11:00 | TERRA_M-M | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7a66b9e5-cb39-34d8-8d67-76ed4e78d1f9 | -20.75457 | -48.51891 | 2024-10-09 01:11:00 | TERRA_M-M | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1d059d1a-8ec7-31f9-bd4c-2e138067c45d | -20.74556 | -48.52047 | 2024-10-09 01:11:00 | TERRA_M-M | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 3011ace6-485b-3a9f-bdb2-73fb3f7d459e | -20.68221 | -47.18064 | 2024-10-09 01:11:00 | TERRA_M-M | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b419d647-d447-371a-ad3e-ebd0f59df52d | -20.66534 | -45.90753 | 2024-10-09 01:11:00 | TERRA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 2a59be95-c37e-3733-bf1c-184d75e6ce31 | -20.66331 | -45.89502 | 2024-10-09 01:11:00 | TERRA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 724b0c04-586e-3a96-b679-5adb4c566a99 | -20.65309 | -45.89743 | 2024-10-09 01:11:00 | TERRA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 31f98889-4826-33c7-8142-aef53d59664b | -20.63662 | -45.92631 | 2024-10-09 01:11:00 | TERRA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4f96475f-fd2b-3b97-8f80-cacc009840fc | -20.61779 | -49.35685 | 2024-10-09 01:11:00 | TERRA_M-M | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0cbacc06-6238-3959-9fa3-77baf123f039 | -20.60891 | -49.3583 | 2024-10-09 01:11:00 | TERRA_M-M | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f2cefdc6-7112-35fc-ab8c-869ff5a8b7ac | -20.60004 | -49.35977 | 2024-10-09 01:11:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 57aa1e62-afc0-3616-82ca-ada020b75271 | -20.59869 | -49.35031 | 2024-10-09 01:11:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f8b85012-a34b-3883-98ad-cf124ff31b85 | -20.56763 | -50.11924 | 2024-10-09 01:11:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 0328816d-ed6a-3f76-aef3-3ddd113ecea4 | -20.56633 | -50.1098 | 2024-10-09 01:11:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 3bbe1189-5a91-3de5-912c-07ed2e36f0fc | -20.56007 | -50.13008 | 2024-10-09 01:11:00 | TERRA_M-M | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 50edc470-2995-3dc0-9260-fd519d8fda7d | -20.55877 | -50.12065 | 2024-10-09 01:11:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 2871cd33-6ce1-3389-8b32-9b43a860a1e4 | -20.55746 | -50.11121 | 2024-10-09 01:11:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |


[Clique aqui para ver as próximas entradas](README27.md)
