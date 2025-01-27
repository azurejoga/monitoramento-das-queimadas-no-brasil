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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c1b0b24-c703-3db6-b4ed-9fb6af5f8b75 | -11.10106 | -43.34165 | 2025-01-27 04:53:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce4edf50-bb82-336a-92e7-a87d2ea0404e | -11.52079 | -54.37884 | 2025-01-27 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00697e3b-d600-3c83-86e4-97b39a309516 | -17.29395 | -53.76731 | 2025-01-27 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45d7c378-78e2-32ec-8fa5-b4a1f93fd9e8 | -15.24689 | -60.21928 | 2025-01-27 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 342b06eb-41c0-3ae2-9263-b9fbb360a099 | -8.80299 | -49.81369 | 2025-01-27 04:53:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75bb259d-1b7e-33a2-907d-8b1a487f00c4 | -8.11669 | -43.13177 | 2025-01-27 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| be301e56-a489-3bbf-9243-a2738261080d | -5.23976 | -56.06294 | 2025-01-27 04:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5788b6c-d39f-3858-8133-6e3aefdd83dd | -17.29675 | -53.77155 | 2025-01-27 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3d888c3-bc55-31d8-a55d-c52ebefa1ea5 | -17.29285 | -53.77469 | 2025-01-27 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbf64703-ef09-3fc0-8da0-f3cf70ef4c03 | -8.80187 | -49.79627 | 2025-01-27 04:53:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88e655af-d7be-3ea6-9acf-f3beac50dcbe | -15.03418 | -57.18828 | 2025-01-27 04:53:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1eb7f73-fb8f-36b0-a661-d6e32251ab9c | -16.3914 | -51.2681 | 2025-01-27 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2546fa2e-0c07-3307-84d8-aa973550764b | -17.2973 | -53.76787 | 2025-01-27 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15dc1645-9630-3ec4-bc44-0a5ae1c08085 | -8.59289 | -49.5141 | 2025-01-27 04:53:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21c8b879-b3c9-3a00-8a7c-5cd28b647551 | -9.34347 | -49.54641 | 2025-01-27 04:53:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dc1679e-7c17-3c7c-b539-d49418711130 | -19.02202 | -57.6204 | 2025-01-27 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.2 |
| 61a7cc3e-23e7-3c2f-9c1f-aad66c7be5d8 | -12.70141 | -54.87481 | 2025-01-27 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd708e72-8f8b-3645-8d2d-7bafe55d8441 | -12.56203 | -57.75747 | 2025-01-27 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e37b6e52-a9f6-3db7-9e95-48e7c509f2bf | -12.70835 | -54.93833 | 2025-01-27 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2144de3d-9a78-3c93-8d49-6c8156b4f935 | -12.56127 | -57.76199 | 2025-01-27 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 46cceaed-acca-32ff-8aff-9adb511da396 | -19.11482 | -56.21819 | 2025-01-27 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 80e10dd6-a842-37a9-b62e-ed23d5fe668d | -21.74436 | -56.76425 | 2025-01-27 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8e146e6c-0132-3152-a2db-1ea0e58e6564 | -12.85281 | -58.31038 | 2025-01-27 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 531cec5d-b195-365a-b321-b7df67f61464 | -13.78468 | -50.78794 | 2025-01-27 04:55:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2ef8317-1036-321e-bcfc-a16598850b63 | -12.56574 | -57.75813 | 2025-01-27 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b403d2a-3576-35f9-bbbd-0ee67f26bf57 | -13.48353 | -52.94897 | 2025-01-27 04:55:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f65a7b78-cead-3d3b-9763-d24a9b90c971 | -13.48073 | -52.94481 | 2025-01-27 04:55:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daee0fcc-a762-32f2-9842-180863e21a0c | -12.71167 | -54.93888 | 2025-01-27 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4d400b78-9ddc-3937-a998-aee1fd6b591d | -13.48407 | -52.94534 | 2025-01-27 04:55:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc6e306f-7d03-3821-93b3-c88fd00c705f | -12.69913 | -54.8891 | 2025-01-27 04:55:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a179abed-0539-329c-bf9a-8f449c8ce538 | -12.55755 | -57.76133 | 2025-01-27 04:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f75ba2ba-a3db-3a26-aad3-747866fe6f96 | -30.15159 | -52.02639 | 2025-01-27 04:57:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 8c11f87f-58bb-3e14-904b-ec972d199832 | -30.44854 | -54.17683 | 2025-01-27 04:57:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| b83e3ece-dfb2-3159-ac8c-a781928d09c9 | -29.29987 | -51.32703 | 2025-01-27 04:57:00 | NOAA-21 | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c16d903-a4f7-3d1d-972c-3de15a5ff79e | -3.38617 | -53.23936 | 2025-01-27 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cec173a7-a3b8-30e5-8f33-cff905472c9e | -3.38673 | -53.23572 | 2025-01-27 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a23abbf1-82f3-3931-a7cc-ec5c6a9980ff | -3.45677 | -52.8634 | 2025-01-27 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ad02638-4045-3f39-b16f-daa66b6cc408 | -2.90824 | -54.28816 | 2025-01-27 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb707af-8d88-3d0c-9550-d13e554ee812 | -3.46098 | -52.86406 | 2025-01-27 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dec4ef6-ab4a-306b-848e-23adf7c6f531 | -9.26065 | -60.31331 | 2025-01-27 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bf29d87-6d9c-34fd-b032-64b7a25d542d | -9.26009 | -60.31683 | 2025-01-27 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dac6bc6c-3e1f-3ab9-b02f-b089ec6fbfff | -5.23689 | -56.05966 | 2025-01-27 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e95afd57-c813-3395-9671-15d7881568f6 | -5.23627 | -56.06371 | 2025-01-27 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e768055c-9e76-316f-aea5-785618b52bc4 | -15.24237 | -60.22316 | 2025-01-27 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5249c742-f916-32ab-8ebd-29bed9f5502f | -17.29669 | -53.77345 | 2025-01-27 05:20:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35adfc50-69a4-31be-9926-37fd4861f86e | -15.24629 | -60.22006 | 2025-01-27 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69520b48-1345-36f9-abc9-64ef48120d30 | -17.29185 | -53.77277 | 2025-01-27 05:20:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 329f2434-e196-39c6-acc9-4d53eb6adc65 | -13.48193 | -52.94571 | 2025-01-27 05:20:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b847f96d-e117-3306-abce-47bd4900981a | -12.55822 | -57.759 | 2025-01-27 05:20:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d7eb9065-409e-30ed-aaa8-b340f8501add | -15.03381 | -57.1884 | 2025-01-27 05:20:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c949fc97-42d1-3248-aaab-ceb1c3c4b863 | -17.29247 | -53.76744 | 2025-01-27 05:20:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee9b7ac6-e6b6-3ca0-92df-94bf9c1d2f8c | -17.29731 | -53.7681 | 2025-01-27 05:20:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d273d402-7394-309b-9c03-ab33ca7b60ae | -15.25356 | -60.21751 | 2025-01-27 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c7799ce-0b9b-3ba0-a289-75127424ad49 | -15.25412 | -60.21386 | 2025-01-27 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7e19232-6644-3df4-810b-af569aae2965 | -12.85094 | -58.31107 | 2025-01-27 05:20:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bff7902-56e2-3c27-bd2a-e6f33b7835ba | -15.24293 | -60.21951 | 2025-01-27 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b3fce9f-3f78-3446-a7de-71502c08aa73 | -12.56534 | -57.76009 | 2025-01-27 05:20:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e05fd3fa-806f-3980-b699-b96d7cd9c39c | -15.2502 | -60.21696 | 2025-01-27 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ae5514e-a83a-351f-a55f-fd7ad7a6cba9 | -12.56178 | -57.75956 | 2025-01-27 05:20:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 165370a9-b9c4-356d-b998-63af6236fdad | -8.11469 | -43.13367 | 2025-01-27 05:22:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 9d1b172f-0d4f-3750-9350-c33126fd2551 | -8.11605 | -43.1245 | 2025-01-27 05:22:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 516473c5-8878-31b9-95e2-b58a1f0dd7a8 | 4.32144 | -60.68401 | 2025-01-27 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70924aee-7db1-35df-a92a-4923d9826bac | 4.32393 | -60.68402 | 2025-01-27 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db72ff47-8e04-37e8-924b-b0176981fd8d | 1.17773 | -60.5 | 2025-01-27 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ae31748-6d31-3262-b476-bb1aaa8e11f1 | 4.32431 | -60.67977 | 2025-01-27 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6df4a864-9a15-317a-9900-3a157e9c1995 | 4.3233 | -60.68016 | 2025-01-27 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9c273a9-958f-32e3-8e82-09cc888efe2c | 2.44561 | -60.63707 | 2025-01-27 05:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 541f6c6b-f119-3e2c-b142-fe84ac964dc8 | -5.23721 | -56.06361 | 2025-01-27 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a86e32de-5170-3a96-b89c-1c049c9d779a | -9.26238 | -60.31455 | 2025-01-27 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10346283-1a7a-3ff1-b1c0-89b73ddaf1d7 | -9.25761 | -60.31786 | 2025-01-27 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 203cf0db-99bb-358c-b218-9e4c04f9ed9a | -12.56308 | -57.75832 | 2025-01-27 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2622c8b3-8ddf-3d90-bd58-a4eeccde00db | -9.25817 | -60.31397 | 2025-01-27 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02554558-5aaa-3872-9e50-e899cebdd48d | -9.26181 | -60.31846 | 2025-01-27 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daf3994d-5ad2-3d43-bdb9-547780732c2b | -12.56268 | -57.7616 | 2025-01-27 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21383664-3cf7-3cdd-b143-d14760391655 | -12.55743 | -57.76093 | 2025-01-27 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c25fd101-5db4-3cb1-93f8-d75a86bc6804 | -15.2522 | -60.2178 | 2025-01-27 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e1b4f4f-23c5-30e4-8cac-d1cb0a005d26 | -15.24759 | -60.21711 | 2025-01-27 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1234fd03-693a-3785-8194-de622b55f58c | -15.24236 | -60.22147 | 2025-01-27 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e155dbca-8cb5-32cf-b423-a69f4219029c | -15.39 | -43.78 | 2025-01-27 12:00:00 | MSG-03 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 11733a12-a196-3f71-9db3-4ff9c213bdfe | -15.42 | -43.79 | 2025-01-27 12:00:00 | MSG-03 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8d565012-a4f6-3916-9b49-e75cee7cfc6b | -15.73 | -45.95 | 2025-01-27 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |


