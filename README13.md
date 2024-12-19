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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e740b365-7ebe-3213-b639-4f1372976681 | -4.35186 | -48.47606 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9232990a-11a5-3c0f-a321-bf154f9ade16 | -11.79 | -58.02381 | 2024-12-19 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af0e2c37-96c3-31da-95d5-61b7d1ab611e | -12.23037 | -54.3133 | 2024-12-19 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e1888f29-88b5-33a3-a04a-48b678f5fe74 | -13.92218 | -54.6176 | 2024-12-19 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9ebeac32-eed4-3973-9602-2ab45005b5b1 | -12.22554 | -54.31267 | 2024-12-19 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b4a9b7e8-cd46-3551-aa8b-ee35355c0118 | -10.51009 | -49.1261 | 2024-12-19 05:25:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 536ebdd3-69e2-3ad3-8a50-aea242d6444d | -15.16866 | -56.46511 | 2024-12-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| afd4de7b-f5ed-3661-a550-b64e4528b5c5 | -14.52612 | -59.97056 | 2024-12-19 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed071962-b215-34bd-a170-14ab6c894fdf | -4.33539 | -48.29955 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9655683-42c0-3de1-9364-95449d9780d7 | -4.3283 | -48.30334 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5dc92e3-c969-35db-b327-542dfb551a88 | -12.22661 | -54.3106 | 2024-12-19 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 872367d7-b22c-3e34-8008-cd82d991c655 | -13.8932 | -54.61332 | 2024-12-19 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a5cfdd06-b193-34cd-b541-aefe24c7a557 | -13.49005 | -52.94831 | 2024-12-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b4a6771-0a7d-3660-8ce0-7b9d6801e92a | -11.43565 | -55.88725 | 2024-12-19 05:25:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cabd9d5-8a0b-3bfc-b8fc-add462acd15f | -3.50199 | -53.95518 | 2024-12-19 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6278654-7171-32d9-8305-89bf151e0b13 | -4.34908 | -48.47588 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9abfc335-158b-3d86-a65d-39f8fe54c1e5 | -15.1681 | -56.46944 | 2024-12-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 742c5b34-e1fd-3dd4-a69a-b3b051e95216 | -12.55596 | -57.71387 | 2024-12-19 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3debd8ef-6e5d-3123-a89c-2cd9148fe13b | -12.15936 | -58.14864 | 2024-12-19 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b838953-63ee-36de-b0e9-ab3500bf88ba | -12.22591 | -54.31591 | 2024-12-19 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8635d7ae-702b-3278-9d35-7bf1df0f4609 | -4.34983 | -48.47079 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bafd4a7-c1cf-369c-beb5-3b624f2e72f3 | -15.16544 | -56.46665 | 2024-12-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e79e3fac-4ba0-3de0-b136-779b150b108e | -10.50517 | -49.1259 | 2024-12-19 05:25:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d361005e-9b00-3cb7-9bd4-019f5e9cd368 | -13.89254 | -54.61885 | 2024-12-19 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be49b3b8-89b2-3617-b97f-86a8b69caf73 | -4.35542 | -48.47689 | 2024-12-19 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9879ba70-5828-383a-9a42-bf3298d4a002 | -14.57151 | -57.01292 | 2024-12-19 05:25:00 | NOAA-21 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| caf4265c-e37c-370e-b997-6887f0ddfba1 | -15.23723 | -59.92456 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f28cee7a-d012-35d0-b6ea-adfb97d7b095 | -19.0612 | -52.88974 | 2024-12-19 05:27:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24fbc4a4-8fed-3e14-93ac-e6be76a790ab | -15.49113 | -60.0452 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9c91d15-2f9f-3ec5-8aec-c0f5868d85e4 | -15.23484 | -59.91575 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51defea0-d4bc-3358-a598-5b3fd2dacd77 | -18.73725 | -56.55865 | 2024-12-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a282adb7-7949-3257-8308-51d2abb977db | -20.78099 | -49.85957 | 2024-12-19 05:27:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 57354dcc-5a81-3432-b62a-7e5095920193 | -15.23664 | -59.93041 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74556cb7-0118-3ed7-938e-dae2ae4b136e | -17.29821 | -53.76635 | 2024-12-19 05:27:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6599168a-1d4b-3b7c-b86e-91edc27c7185 | -17.97431 | -54.00427 | 2024-12-19 05:27:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd76d5b8-92ab-3bb7-8bbc-1cc1fbdd1a54 | -19.12597 | -53.45934 | 2024-12-19 05:27:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aee6547a-6fb7-3c9d-adc4-6fc5338416e1 | -15.23724 | -59.92628 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60a1a6c6-7ce4-3e55-a26c-48c4ed0393e5 | -15.37959 | -60.31447 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66608156-b1c2-3251-8ee7-e74abbe4c5ed | -15.23844 | -59.91803 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e96f586-1f12-3cc7-9370-b40e76b5b753 | -18.74178 | -56.55926 | 2024-12-19 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d3f5b15b-02b3-3f97-9fd1-c6b7e5e12a43 | -15.23665 | -59.9287 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f23bde1e-8a45-308a-a826-879ca28fd4c7 | -15.23784 | -59.92216 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a71e417-ef9b-31c5-9320-2de19a1e0931 | -16.21125 | -59.92809 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c0b62e1-61f1-3715-bb02-ae4699e165a5 | -15.2349 | -59.91749 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99a15985-a6f0-3e48-a661-3ce03243a58c | -20.78152 | -49.85238 | 2024-12-19 05:27:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 471eab7f-4a34-3c66-bd99-07989ef596bc | -19.06701 | -52.89018 | 2024-12-19 05:27:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f19ffbec-a0f2-3bd5-b99b-22a8457b6f53 | -17.97467 | -54.0009 | 2024-12-19 05:27:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffd3d1de-e6a9-3002-82eb-4dbed55e7f69 | -17.30139 | -53.76871 | 2024-12-19 05:27:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57ade5f9-c01c-3abe-aa2f-13cc6e390d62 | -16.2089 | -59.92952 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c15c754-2f22-3f36-b58b-4efed258c7c3 | -15.23781 | -59.92044 | 2024-12-19 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bc6e546-fa59-3115-9771-470b365e5810 | -19.12756 | -53.45795 | 2024-12-19 05:27:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da73ee7d-0b3e-37ed-8039-90e54bd08adf | -17.97395 | -54.00763 | 2024-12-19 05:27:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa76aa96-7c16-35f7-8753-6b0daf428f65 | -29.73686 | -51.1514 | 2024-12-19 05:29:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 5.9 |
| 1887f73e-2d17-320a-8258-c788168a2c8f | -5.2108 | -43.3067 | 2024-12-19 05:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d6ec3155-e364-350e-8f99-5eec391f35db | -5.2108 | -43.3067 | 2024-12-19 05:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 18348630-10cd-324e-94c5-2b8f805d9fc9 | -1.55497 | -53.7757 | 2024-12-19 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d11ad97c-322b-3096-af48-10f919b84bca | 2.28028 | -61.22757 | 2024-12-19 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2174440a-9da4-3c26-ac58-1512953a1026 | -1.56126 | -53.77866 | 2024-12-19 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92212609-9567-32b7-b80c-4a7489daa794 | -1.56144 | -53.77693 | 2024-12-19 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 658bf6af-1ea9-37c9-b02a-fee922d5a22c | -1.56789 | -53.77825 | 2024-12-19 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a984c049-81c9-31e7-940d-000a37d266c4 | -1.5548 | -53.77746 | 2024-12-19 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dfc55f6-89c0-39f1-a01b-45ebb6c6718a | -1.56771 | -53.77995 | 2024-12-19 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33a0034f-eff1-33a9-bc20-a93472e03681 | -5.2108 | -43.3067 | 2024-12-19 05:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 91a30283-e7b9-3db3-812d-fd77e3fa301c | -1.26708 | -54.13001 | 2024-12-19 05:50:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3c0499ba-b311-3faa-8b77-e71d0d593dcb | -12.22531 | -54.30853 | 2024-12-19 05:50:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7bd6002-8251-38aa-8e70-0bd3071af261 | -12.23176 | -54.31631 | 2024-12-19 05:50:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac1e627c-a617-31d1-98ab-0b704fa77e5b | -12.55914 | -57.83068 | 2024-12-19 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faf72af4-665d-3534-a822-ef60fc1e78c0 | -12.55961 | -57.82662 | 2024-12-19 05:50:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b6ce91-d071-3549-aeb6-9b3e3460d00f | -15.1683 | -56.46227 | 2024-12-19 05:50:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f708114c-d0f1-3188-85be-4f38b37cfb2b | -12.23252 | -54.30919 | 2024-12-19 05:50:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7533704a-3452-3b27-91a5-ae8e22783a9a | -12.22455 | -54.31558 | 2024-12-19 05:50:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32dd870b-a256-3238-bc9e-2906a02c7bcc | -15.16771 | -56.46805 | 2024-12-19 05:50:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8da913c7-22d3-32b7-9226-2c0b8768216e | -4.34718 | -48.46899 | 2024-12-19 05:52:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c965becd-b3b6-304b-8760-3e9c2cad4538 | -10.49667 | -49.12158 | 2024-12-19 05:52:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0caaae12-98c3-3901-bdc2-9ecbafb085f8 | -5.21062 | -43.30123 | 2024-12-19 05:52:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 1a87a27e-5013-3c11-bedb-83e78083955f | -5.20948 | -43.27262 | 2024-12-19 05:52:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 46ac7493-b5f3-338a-95ff-d9d487da45e5 | -5.20531 | -43.30494 | 2024-12-19 05:52:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| be6b0bcd-231b-3414-8631-49bfba07774f | -13.30781 | -52.44073 | 2024-12-19 05:54:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0a9821cd-c223-33c0-bb83-420cf83ca924 | -13.91973 | -54.60816 | 2024-12-19 05:54:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 9aabfe03-a5cd-3550-a509-2d7e071d3788 | -12.22876 | -54.31047 | 2024-12-19 05:54:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 31554740-7b64-3051-b194-44f54d623bc7 | -13.92109 | -54.59912 | 2024-12-19 05:54:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3b25383d-3b81-3f2e-8340-1d2be2c60690 | -15.16536 | -56.47253 | 2024-12-19 05:54:00 | AQUA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d35b5f48-5f38-305b-9808-e2aeb907512a | -13.91835 | -54.61723 | 2024-12-19 05:54:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d62087cd-57ae-39cb-98e7-c0db3b2d38a4 | -13.89182 | -54.6131 | 2024-12-19 05:54:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 762521ac-431d-3e50-ae80-8d1c7aad2bf0 | -13.3092 | -52.43102 | 2024-12-19 05:54:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0262c975-469a-3cde-8c0f-689ee5bd0a8e | -15.15771 | -56.46102 | 2024-12-19 05:54:00 | AQUA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0aa25550-f726-3ba7-947f-eebdbb88c33e | -12.21991 | -54.3091 | 2024-12-19 05:54:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fbbeea20-455e-3727-a3c2-8268eb656220 | -15.16696 | -56.46253 | 2024-12-19 05:54:00 | AQUA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 70e624ec-2850-3811-a5b3-58c3405c1bfe | -3.2197 | -45.4949 | 2024-12-19 06:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 983e7eae-54ab-35d5-a8a0-626b29022a2e | -3.2383 | -45.4941 | 2024-12-19 06:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ad34aa7e-5500-33fc-a0b9-ebc9decca41c | -3.2383 | -45.4941 | 2024-12-19 06:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8b8cb4fa-6e69-3967-8ba6-9078f9b687aa | -5.8333 | -35.4902 | 2024-12-19 06:10:00 | GOES-16 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 80.2 |
| d24f1f23-17c3-3277-8b0a-c0b694f55a02 | -5.8336 | -35.463 | 2024-12-19 06:10:00 | GOES-16 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 68.2 |
| d5f632bf-9b1f-38b7-ba17-86c9ab06faeb | -3.2197 | -45.4949 | 2024-12-19 06:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ad26c197-3665-326d-bd68-c6970c04222b | -3.2383 | -45.4941 | 2024-12-19 06:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1b59ef77-9f75-3e3a-b738-bbc64ef49b17 | -3.2383 | -45.4941 | 2024-12-19 06:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a66a8cf3-4233-3e46-a6e7-43a88f6ba38e | -3.2383 | -45.4941 | 2024-12-19 06:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0d34de10-f3a3-3d0a-b633-626a9e1c1fe8 | -3.2383 | -45.4941 | 2024-12-19 07:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a8280f99-8f8e-3343-a6d2-8c8c7ccfdbe9 | -3.2383 | -45.4941 | 2024-12-19 07:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9e0697b3-2d1c-3bf7-8b6f-6f6f115b8af0 | -3.2383 | -45.4941 | 2024-12-19 08:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |


[Clique aqui para ver as próximas entradas](README14.md)
