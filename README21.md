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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89fc8663-a02d-3d7d-a75d-ae08577e3aa3 | -21.5684 | -48.4942 | 2024-10-04 00:57:05 | GOES-16 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e8966452-58ad-33f0-9dbb-7cbed8bdb1dd | -21.7988 | -48.3691 | 2024-10-04 00:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 94.2 |
| de88062d-b070-3cb8-b931-0a4451b7739a | -21.8175 | -48.4346 | 2024-10-04 00:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f433c831-d52f-30ff-b7f9-86420a40f667 | -21.8189 | -48.3876 | 2024-10-04 00:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 83.8 |
| faf8022c-4591-3d45-93f3-2f45efbcec4c | -21.8196 | -48.3641 | 2024-10-04 00:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 0c1a7b4f-8dad-3550-afdb-1d4ad4339091 | -21.8376 | -48.4531 | 2024-10-04 00:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 9fbd53a9-8c0f-3200-997d-d8789eb8806a | -21.8383 | -48.4296 | 2024-10-04 00:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 7007dd66-0935-3904-8a4b-5b7a39933ebb | -21.29 | -48.93 | 2024-10-04 01:03:22 | MSG-03 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4b0e783c-ced2-30d0-9e1d-e6d5b1f51921 | -21.29 | -48.87 | 2024-10-04 01:03:22 | MSG-03 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7af9ed3c-3768-3d77-9eb2-cd50f8bc83ac | -21.33 | -48.95 | 2024-10-04 01:03:22 | MSG-03 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 61c89e2b-56b6-3958-80ac-06d14494b109 | -21.32 | -48.89 | 2024-10-04 01:03:22 | MSG-03 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3c22f7-2b5a-35c3-a04a-77c5193d22a2 | -21.32 | -48.83 | 2024-10-04 01:03:22 | MSG-03 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6daf9f78-682b-3691-a99a-be8d6f1e6faf | -21.36 | -48.91 | 2024-10-04 01:03:22 | MSG-03 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 01e7ebeb-1fa5-3e08-8887-3055f850dc68 | -19.31 | -42.62 | 2024-10-04 01:03:32 | MSG-03 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc93b981-b00c-324e-800c-b0805fdc3a81 | -17.0 | -56.76 | 2024-10-04 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc018705-bbbf-344d-9984-11eb196daf1a | -17.03 | -56.78 | 2024-10-04 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db1777ed-2fce-310c-89b3-8a8867f08009 | -4.67 | -45.91 | 2024-10-04 01:04:59 | MSG-03 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bbd2082-e989-3fad-932f-4987af195c10 | -4.67 | -45.86 | 2024-10-04 01:04:59 | MSG-03 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa83563-6235-3c0e-9eac-909808906123 | -3.1052 | -50.4783 | 2024-10-04 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 354c528a-fb52-3169-8ddf-49ac9a1e1f39 | -3.2349 | -50.3695 | 2024-10-04 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0a024a12-88c7-3a94-bb85-8d0c54c3882a | -4.0949 | -48.4894 | 2024-10-04 01:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 271d02f3-5e67-35c4-9ded-9ad0668af963 | -4.095 | -48.4679 | 2024-10-04 01:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 83ed47cb-1fa9-3858-824e-f25e8e71d4b1 | -4.4657 | -42.8877 | 2024-10-04 01:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 73ace1a1-849c-3c92-86a6-8fbe313af3e0 | -4.5375 | -43.304 | 2024-10-04 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| a274fe1d-1530-3af2-b89f-52a780ef0f8d | -4.5949 | -45.7436 | 2024-10-04 01:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 80821cca-ba24-38b2-97e4-fdc3bf6ada25 | -4.6684 | -45.8961 | 2024-10-04 01:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 34.7 |
| d42c812e-02e3-3f93-b26f-5c863af0d06c | -4.6686 | -45.8738 | 2024-10-04 01:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| b3a0418f-ba76-39b3-9ce0-7a082e185b7d | -4.687 | -45.8951 | 2024-10-04 01:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e3d1593b-29c9-3b47-85be-8e2444696bc0 | -4.6872 | -45.8727 | 2024-10-04 01:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 212.3 |
| f7656a1d-4112-3ac9-a153-370aaf8de639 | -4.6873 | -45.8504 | 2024-10-04 01:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 43.7 |
| b514dc88-780e-35c0-9b31-ba16160d14ef | -5.5031 | -48.8261 | 2024-10-04 01:05:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 946e74c9-a3b7-3a34-9fe1-e6b96e2fbafd | -5.5033 | -48.8046 | 2024-10-04 01:05:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 8de71601-abc9-3945-ba5f-9408bd1ee143 | -5.8214 | -44.1426 | 2024-10-04 01:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 22e58fb2-5384-3d58-8d3c-23115c5f10d6 | -5.8216 | -44.1196 | 2024-10-04 01:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f235cb96-d7e3-37f2-9729-bc762f815c53 | -5.9599 | -45.3861 | 2024-10-04 01:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 79e48aa4-048a-3e9d-b9fe-baa5bc6cb9d8 | -7.0529 | -71.7726 | 2024-10-04 01:05:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 182f05d2-d53c-3945-8833-4442b0be70c0 | -7.0529 | -71.7544 | 2024-10-04 01:05:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 95130184-78db-32c7-99f3-110a914ae851 | -7.3821 | -72.9355 | 2024-10-04 01:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| ee36cdb3-bde6-3e24-9586-28ea4eaf71e8 | -7.3821 | -72.9173 | 2024-10-04 01:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6ae58c41-ded8-37bc-8074-e3d291e4aba9 | -7.8539 | -45.3611 | 2024-10-04 01:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ba3ec9b9-409e-3419-83b1-3735bfbfde59 | -7.8541 | -45.3384 | 2024-10-04 01:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0b0cb9cb-b04e-3cdf-bf7e-455d76e46765 | -8.6448 | -50.0518 | 2024-10-04 01:05:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| fc762a41-d84d-3aea-b616-e5fc3c118d02 | -8.6636 | -50.0501 | 2024-10-04 01:05:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 92935748-f3b1-3f54-aef2-1c65bc74ccf4 | -8.6676 | -66.6391 | 2024-10-04 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c22a214a-88d7-3d9d-b0ac-d120fbda9a5f | -8.6677 | -66.6205 | 2024-10-04 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9eec3f11-68ae-32bd-9efd-a93aeb6ead37 | -8.6677 | -66.602 | 2024-10-04 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f77d759c-c008-38e4-b3c2-d273fd512ce3 | -9.0162 | -67.3904 | 2024-10-04 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| e694ea27-3cd9-33ec-8103-90a2f1330ca3 | -9.0898 | -67.4997 | 2024-10-04 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 2dd0f5b0-f068-3447-9b46-a52e063f9884 | -9.3115 | -50.8203 | 2024-10-04 01:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 34a8bfc1-423b-3b6e-a171-dfe34064a80f | -9.3118 | -50.7991 | 2024-10-04 01:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 209.3 |
| fdc5c41a-81fd-34cf-b6f1-d8d3479fab76 | -9.3303 | -50.8186 | 2024-10-04 01:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 0da74285-a474-323d-8352-6c9924b9b99d | -9.3306 | -50.7974 | 2024-10-04 01:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 189.2 |
| d3c7e6ff-0ee3-367e-bead-58c66fff6b98 | -9.55 | -64.2179 | 2024-10-04 01:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 64b860f2-528a-313c-bcb7-890d31c3d4dc | -9.5686 | -64.2171 | 2024-10-04 01:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 71861b70-2c77-35d4-96ce-ffbd6c6f55b4 | -9.9375 | -64.7675 | 2024-10-04 01:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| b025ecfc-a34a-3dd1-8476-ce22d56b71d6 | -9.956 | -64.7856 | 2024-10-04 01:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7ad3a2e3-2583-3f3e-9c4f-04850ef120de | -9.9561 | -64.7668 | 2024-10-04 01:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f9dfb925-7064-3df5-b1a2-284f5857290c | -9.9747 | -64.7661 | 2024-10-04 01:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b0c06f3a-de52-345f-acb6-1e60fcb75f5a | -11.0536 | -46.5118 | 2024-10-04 01:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 213a9325-c2f9-38ae-b92e-5d008f337fab | -11.2181 | -46.9397 | 2024-10-04 01:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bea5e7e6-2fcb-3871-aae0-7f646cc2ea99 | -11.5425 | -65.0607 | 2024-10-04 01:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1aa4fe69-23c6-3a5d-8f84-9c4ea6e814c6 | -11.5992 | -65.0015 | 2024-10-04 01:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a152e8da-b5a1-335f-857d-d15d5b70d2cf | -11.618 | -65.0007 | 2024-10-04 01:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| fbc9f577-2027-3432-9824-80feefeff1fc | -11.6181 | -64.9818 | 2024-10-04 01:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 568dcdd3-9db8-3b90-adaa-a7a29adbab48 | -11.6369 | -64.981 | 2024-10-04 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.7 |
| d7e3d29a-b71c-36a8-a368-dc48ee333475 | -11.6932 | -64.9785 | 2024-10-04 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 135.6 |
| fd5eca7f-9926-30ee-ae7e-5f27c49b256c | -11.6933 | -64.9596 | 2024-10-04 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| af0a9bc7-fec0-3bc1-bb97-30cb4ab830c4 | -11.8052 | -56.6024 | 2024-10-04 01:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e880195f-e1ab-3edb-99f9-06af6cbd6741 | -11.8242 | -56.6009 | 2024-10-04 01:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 09ca26f8-2853-32cc-996b-a7d4f5cd0abd | -11.8244 | -56.5808 | 2024-10-04 01:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 2e93f231-ee2b-3770-a404-1e90b7328979 | -11.8957 | -56.9554 | 2024-10-04 01:06:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 40261ed2-f0c5-31b9-9321-b1b3a90c57da | -11.896 | -56.9354 | 2024-10-04 01:06:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 20504c95-8a80-3ac5-8073-3087e77ddd1d | -12.5898 | -53.1359 | 2024-10-04 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 1d75162d-e248-31b3-9cf2-f909f977722a | -12.5901 | -53.115 | 2024-10-04 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 179.5 |
| d2f4e553-2609-3f91-9818-dc3bc1cc2d68 | -12.6092 | -53.1129 | 2024-10-04 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 5e6ccd43-430b-3245-8050-51d7fd1e1b2d | -12.6295 | -63.1225 | 2024-10-04 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 16107df7-085c-394d-8ad1-e8962f5c76c4 | -12.6296 | -63.1033 | 2024-10-04 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 96e34206-1183-387c-af24-34e8c58a568e | -12.6484 | -63.1214 | 2024-10-04 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 306cdecc-9940-350f-9052-62951cf102ed | -12.6486 | -63.1022 | 2024-10-04 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 438a4655-c7ad-3c38-a799-6e5c7e21f589 | -12.881 | -62.4538 | 2024-10-04 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4ed50181-5b92-3993-8fc4-cb70384db320 | -12.8999 | -62.4527 | 2024-10-04 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 16c8b7b4-9776-3139-9d3c-0817d1bfd2c4 | -12.9186 | -62.4901 | 2024-10-04 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| fb95847f-2bbb-3b5d-b61b-bcaccc7ba7db | -12.9187 | -62.4708 | 2024-10-04 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 33c55c5c-cbb2-3ba7-b521-99e3c536eea7 | -13.0971 | -51.1789 | 2024-10-04 01:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 5a034bb2-bb22-3b7a-ab16-6ac011e49d9a | -13.0975 | -51.1575 | 2024-10-04 01:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 44ad1fc8-3120-3805-94dd-147988f753c1 | -13.1163 | -51.1765 | 2024-10-04 01:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1a2e959e-e23d-3b2f-9583-aaba05e3df0c | -13.1166 | -51.1551 | 2024-10-04 01:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 2be28d19-34cf-32b7-92de-d7d193f28c72 | -13.9845 | -44.0236 | 2024-10-04 01:06:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 50306edf-9dba-3f84-8cb5-adfb77eda21d | -14.004 | -44.0201 | 2024-10-04 01:06:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 6ca846a4-43c6-3622-98cc-e2a0334871e7 | -14.7939 | -48.0275 | 2024-10-04 01:06:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 139.4 |
| f4856deb-adb4-39ae-9c71-3962660415b6 | -14.7944 | -48.005 | 2024-10-04 01:06:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 627885a3-9f1a-3091-97a0-e70a3abc93fc | -16.4148 | -57.4028 | 2024-10-04 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 50ca3e5d-b7a0-37b7-98f0-e5212cd8935a | -16.4151 | -57.3823 | 2024-10-04 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 2800d305-2bba-3a0c-bf0c-93e8d2ffb404 | -16.4554 | -57.2962 | 2024-10-04 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| e3431042-9836-3bee-a1ea-a734387fe7b7 | -16.475 | -57.294 | 2024-10-04 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 8a36e5d3-9888-3e32-8f29-2054843e755f | -16.5537 | -57.2442 | 2024-10-04 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 21459969-bbef-383e-a2f2-a8f36a8f4ae5 | -16.573 | -57.2624 | 2024-10-04 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 45c42c2d-5750-3682-aa40-66ca9301a265 | -16.5733 | -57.2419 | 2024-10-04 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.4 |
| 96de481f-90f4-325c-90dc-83c522652c8d | -16.5736 | -57.2215 | 2024-10-04 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 9207971a-a6a8-3575-a200-b768a5876b75 | -16.5925 | -57.2602 | 2024-10-04 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |


[Clique aqui para ver as próximas entradas](README22.md)
