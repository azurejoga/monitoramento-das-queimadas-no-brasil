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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47475b82-60b9-3264-8f2e-be92de5d96f3 | -9.12238 | -61.43446 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3280ecd3-f85d-3cdb-bfca-e5961a766b49 | -9.11868 | -61.42904 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 188e317a-17e7-340a-9845-5c4f6909c2ef | -9.11786 | -61.43365 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e883b84c-84dd-3956-87e7-9cb0d34827f3 | -9.09129 | -61.13161 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84ecaddb-48b7-360d-b6ff-123ab934acda | -9.09052 | -61.136 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59cac3df-b796-305c-a242-4966536c0f2f | -9.08685 | -61.13086 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8e300c7-2527-384c-8067-53f4ea742c40 | -9.0125 | -61.5511 | 2024-10-08 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87b644c8-f1dc-34fd-973e-d84b6fb45033 | -8.98503 | -61.4382 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bad57896-f52d-35c4-bab1-a2e66aa35f3a | -8.21863 | -61.20771 | 2024-10-08 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1491af75-cef5-3aac-8d6c-e34efe6d7206 | -8.21411 | -61.20692 | 2024-10-08 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be1dc7b6-ec35-3d39-9de8-94cf2420c009 | -9.746 | -62.33464 | 2024-10-08 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5baf67a0-e300-395a-b4e5-d8ab92dad0de | -9.74509 | -62.33968 | 2024-10-08 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b5715afb-3ed2-3a6b-9792-153ac6b13b2d | -9.74124 | -62.33381 | 2024-10-08 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86073c23-8026-38db-aa0c-fab1f8a55d77 | -9.74032 | -62.33889 | 2024-10-08 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aa1e3d8-c77e-3ccb-b96b-d364b8d8b08d | -10.20998 | -61.95069 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fc6e076-edb2-393b-9e1a-1110617cce7a | -10.20916 | -61.95538 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 049fc1ce-9373-3494-bd3e-f9f892e9eba2 | -10.20862 | -61.95378 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e86e2e2-f57c-3078-841f-f103e42d68a9 | -10.20837 | -61.95989 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf70071a-a820-3820-883e-65448cd95638 | -10.20779 | -61.95832 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1edb6e54-efd0-3784-b946-e09650b7c7fd | -10.20695 | -61.96291 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f06fb2e6-0fe6-375c-99d0-5fe81cd93e0f | -10.20456 | -61.95456 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b31271c2-d530-348e-b6a0-65bc179301e5 | -10.20377 | -61.95908 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e5751e0-0d9e-3e68-89ff-871017b79db7 | -10.20319 | -61.95753 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ca08704-65bf-3703-88b0-6e834a4797e9 | -10.20296 | -61.96371 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f670c55-a70b-3833-abe4-2b735abd2025 | -10.20236 | -61.96207 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a04f8731-d402-3e98-8808-333c38892bb3 | -10.19916 | -61.95831 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f61b232-7b05-3be5-a89f-10f38305d071 | -10.19859 | -61.95674 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6670d31-4c34-31fc-898b-74e421d38365 | -10.19835 | -61.96294 | 2024-10-08 04:57:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef28109f-4756-3822-aefa-e0b80d31440e | -11.88624 | -62.76873 | 2024-10-08 04:57:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b13aedf-f16a-3e33-b124-8f3683fc653c | -11.88586 | -62.7674 | 2024-10-08 04:57:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7880c601-3a7c-300c-a7d2-ac9ca8fdbda4 | -11.88528 | -62.7738 | 2024-10-08 04:57:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb6ea989-261d-3938-88b4-ca9f7db7c30a | -11.88494 | -62.77248 | 2024-10-08 04:57:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1433c8e1-cad1-3009-b7ba-37ac756752b2 | -11.7718 | -62.88129 | 2024-10-08 04:57:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65ae9a9e-219b-3b67-8516-5a4d7ec2b43c | -11.77153 | -62.8831 | 2024-10-08 04:57:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da6523d8-8d0d-3736-939d-8760dd45579b | -11.76677 | -62.88221 | 2024-10-08 04:57:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcf25230-6edb-35c9-811f-49871cc80ff0 | -11.48407 | -61.97485 | 2024-10-08 04:57:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18484993-9080-34a2-baa4-de07c36101fe | -11.48324 | -61.97936 | 2024-10-08 04:57:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b14e19c5-e7ab-3428-ba53-632ebbb1475f | -11.48233 | -61.97669 | 2024-10-08 04:57:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7a892242-6e28-3d86-8e33-3dccc22cf2a8 | -13.04906 | -62.31744 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39ada9d6-bb37-310f-9acd-dff25c77ab6c | -12.75234 | -62.26666 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2bb3715b-48ba-3f57-abf0-15be826726a6 | -12.74786 | -62.26579 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9fb8aa7e-80d6-3dcb-9d7d-f498f83406f6 | -12.74777 | -62.07705 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9599b485-6513-32c8-920b-703629211e60 | -12.74701 | -62.27031 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d5b01228-edde-3b29-a6b0-6eeffe7e7d0e | -12.74582 | -62.26761 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1c62670d-e3b9-3cb0-9eba-66ed76d22eba | -12.99602 | -62.72469 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd352487-6fe1-3cbd-b6cf-aad948440fd1 | -12.99142 | -62.7238 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3016e89a-3ce2-3228-9002-43234900ed41 | -12.98806 | -62.72525 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c1af93-7ec5-3059-af0b-87cac9ab2c7c | -12.98682 | -62.72292 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23e6edaa-99a5-3177-bfd8-97ee0ffdd5c9 | -12.98124 | -62.67688 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d2a6526-fd78-38d8-a3c8-1dfff9447100 | -12.97756 | -62.67817 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bdc848c0-c9af-33af-950f-47f700b2331d | -12.95938 | -62.46861 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f983bc6c-3d7b-3ecd-941a-7d83a5a1d3e2 | -12.91262 | -62.72051 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 775761b4-fb11-38b8-a2ed-f724e8fd9076 | -12.9071 | -62.7245 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e8bf630-1adc-39d9-9341-cf1d1e480f6f | -12.87492 | -62.79408 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f63f76d2-1c4b-3a6c-8811-731f39e81cfc | -12.874 | -62.79898 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cb3fb0b-16c6-32d2-86cf-eec4f5d38c48 | -12.86936 | -62.79809 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1027a240-e3a2-305e-91aa-9ec856113ab1 | -12.86335 | -62.78983 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e03b3752-c699-3243-b970-d426d1cb0642 | -12.85871 | -62.78892 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4156167c-5b5c-3698-ab96-1334e854fde5 | -12.85604 | -62.80367 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9663a1ed-4aa2-30df-80d1-555196f9fe28 | -12.85453 | -62.80029 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ac4381e4-2964-31a3-98aa-5a4b6c5459f5 | -12.8514 | -62.80278 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b72d38b-e788-37af-a856-9a9cfe0bf763 | -12.84676 | -62.80188 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4551f7fc-ea30-31f3-9965-371dd29d1910 | -12.82904 | -62.46025 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 09ace5f2-ed18-3c2b-8ad3-e228615ae068 | -12.8245 | -62.45937 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08ef7ee1-17f9-3170-9288-1b4362ba0115 | -12.82362 | -62.46407 | 2024-10-08 04:57:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e2b29f0-184a-30c0-a2fe-5556a2c42eab | -12.70783 | -62.95053 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ef99d28-3298-3cd5-b967-f468fd28f88f | -12.7059 | -62.96064 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef40488d-0e3d-3a3c-ba98-1d8a057128e3 | -12.7053 | -62.95913 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83323f0e-8af9-31db-a0c8-41ab279afe7d | -12.7006 | -62.95821 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 414e12a0-3379-3d97-a729-3a8e2635564d | -12.69967 | -62.96328 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84e27fef-9b5c-35c9-9cb7-93e0af82efdb | -12.69591 | -62.95728 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2bf6fe52-36fe-3504-b57a-47a93581ac0d | -12.69497 | -62.96236 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1d3fab9-ebea-3a89-b2bb-bfe358cfc0cc | -12.69494 | -62.93609 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6133e153-f36b-3d16-ab15-4611c8739971 | -12.69401 | -62.94115 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25277641-71c0-3580-aa34-36579cdf56ee | -12.69308 | -62.94621 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a41329ab-3e4e-3e41-ad9e-ccb2b2c76038 | -12.69214 | -62.95127 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74f8944b-24b4-3007-948f-a3461495269f | -12.67237 | -63.08526 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a03cfccc-0c9a-3848-bf81-27d2dad7472c | -12.64578 | -63.09612 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc4a2246-0641-3095-b953-4fc782c4351b | -12.63628 | -63.0943 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2409da5-25d2-3313-a899-9b79a00b30a8 | -12.63608 | -63.14827 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbc5b99b-46c7-3ee0-a52a-0aef38580386 | -12.63532 | -63.09948 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b91d6213-81d4-38a5-ab18-a5f2ab049adf | -12.45587 | -63.00754 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 23ba42e3-1d88-3832-bcb7-19751b86e773 | -12.45114 | -63.00662 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9db78064-e40a-3736-87a0-931afedcfd02 | -12.44923 | -63.01695 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a64f5db9-09ed-3375-9372-62c475923755 | -12.44827 | -63.02211 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1d18a1d-8e70-372c-86eb-0a7b788d5057 | -12.44641 | -63.00568 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94f270ae-e862-3c4a-a73a-54504c875e70 | -12.44258 | -63.02634 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c55894cc-04b7-3c98-b1df-ff6983f40753 | -8.67016 | -63.48114 | 2024-10-08 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 495c4548-dd0b-367b-96d7-2e5caeac6c7a | -8.66958 | -63.48435 | 2024-10-08 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f8d5ba0-d539-3474-8b76-c0e48922e120 | -8.61677 | -63.12315 | 2024-10-08 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc2cc099-7abe-34b1-86b5-3577f0227a99 | -8.61622 | -63.12618 | 2024-10-08 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cd2bfdb4-f20c-35dd-950e-d027718e30f4 | -8.61553 | -63.10104 | 2024-10-08 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c1e2046-01ef-3a63-899b-1cf5f8b05b69 | -8.61098 | -63.09711 | 2024-10-08 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cecd653-b9df-384b-9224-92ec05831852 | -8.61043 | -63.10012 | 2024-10-08 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32547670-ed72-3840-95e5-6099a391919c | -8.60533 | -63.09917 | 2024-10-08 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eabaee28-2a96-36f6-9357-2f681b528f12 | -9.71324 | -63.96251 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3783a32e-d415-3469-83a6-586f642d0ebc | -9.70796 | -63.96139 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcb26b56-9f5d-37bc-9faf-7506fb300dda | -9.66427 | -63.12799 | 2024-10-08 04:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fdafc8d-b302-3ee5-9a7f-64d64fa7d74f | -9.59325 | -63.64404 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2c24be8c-444d-3a68-91c9-7ddaddd09cbe | -9.58747 | -63.64619 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README90.md)
