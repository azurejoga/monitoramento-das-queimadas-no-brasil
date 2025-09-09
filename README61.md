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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4108301e-334d-3e68-96f6-5809b2af9bfd | -12.87951 | -62.09834 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 967e80fe-880e-3cbb-8375-ddd78fb6bf67 | -12.81467 | -56.51433 | 2025-09-09 05:23:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4baa3a69-778b-3a4d-b549-177078ec2743 | -12.87732 | -62.09074 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2d59077-7a16-37bb-8d56-cb87174e02ba | -2.51493 | -51.90816 | 2025-09-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67ae9a35-4b2c-3c1b-93a9-5e5daed75bcd | -14.52186 | -53.96441 | 2025-09-09 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1deb64ab-3939-325d-9f0b-f11a1c0f7db0 | -14.44302 | -53.23982 | 2025-09-09 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7363da7e-65fc-3774-b7cd-2ccde3665503 | -15.78821 | -53.53302 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03ac74cc-2f78-3de9-8604-b8dc66714cc2 | -12.84287 | -52.9458 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b143dca-ca34-3bb4-a114-f9ebbe40047b | -14.90749 | -55.8395 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1670d908-531f-3a24-a25a-fa153c2099f9 | -4.99568 | -56.25532 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7c62c7a-2fb6-3283-a18a-43b2a0c2210d | -15.54817 | -48.37514 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0406b73-ea6a-3501-8121-327311154948 | -14.78803 | -48.2261 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5ee8aac-4a4b-3e4a-9d55-d759d34281ac | -15.24444 | -53.77335 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e419f671-10a1-3d4b-a82f-05df01d3387a | -15.53454 | -48.36504 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4380c1f3-e6dd-31cb-b1e9-accd2fb58708 | -7.58303 | -61.67668 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9d0e636-9c51-3e00-9517-a31cb28f3436 | -6.91941 | -62.94308 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b6d22e4-3bbe-3f3e-9405-a20e0897998b | -12.19345 | -53.89456 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ec8097e-6211-3fe6-bc0a-004a0e115785 | -14.7149 | -60.24506 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ebb711d-49dc-3b18-b174-a0daf4471bc1 | -12.95788 | -54.7542 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4dfc8eb-1072-3a31-90c4-70ac276e0dec | -12.35524 | -63.64241 | 2025-09-09 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6662912-a55b-3f50-954b-86b2a604b994 | -13.96253 | -48.2435 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c6bc1af-f137-30fd-b616-cf688c830f87 | -14.73403 | -55.90596 | 2025-09-09 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86015886-56b6-372a-9985-3ff03956f300 | -6.95715 | -62.92963 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bce1e600-ab01-3458-a3fe-3f666ee5c7fd | -14.53612 | -48.76057 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3cdbd9f9-e95b-3fc4-891b-3f7c41e9e9cd | -12.42415 | -64.22768 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b1e935f-f147-3401-b1ca-5da2ed291065 | -15.71875 | -53.53621 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e41ce04-e8ed-3698-80a3-33b0efb34726 | -15.52462 | -48.39334 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2392fb22-e0ea-37b1-949c-8298e38d36fc | -12.41881 | -63.89561 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60a6c92e-27ac-3a38-8cc5-e5a106171934 | -12.92594 | -54.78035 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68c27ed6-cb0d-35f3-aa7e-c7dc19f4c111 | -14.53674 | -48.75455 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb662bba-8b60-3761-9da1-8608f01d8d39 | -6.95245 | -62.9367 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b37d9b61-3e35-3ff7-8820-861d34d8df5c | -15.74104 | -53.52846 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6c3e3f7a-8828-30ce-b5b1-26f929bbd3ab | -5.01328 | -48.46766 | 2025-09-09 05:23:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42087f68-ab16-3c65-afec-53b24c3521da | -12.204 | -53.8902 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 08a96019-369e-3070-a75e-1d70f82374e8 | -4.99151 | -56.25774 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36c13916-0422-3b36-8453-86b21ece53cc | -12.84773 | -52.94985 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 421f3fd4-ea3f-35a2-a246-f5edf2dc5bd9 | -12.83231 | -52.94448 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33fb9054-deaf-32a9-9280-fca38652342f | -15.27174 | -53.80838 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 114864ca-f254-3f1a-836a-e27932f1dd74 | -4.26998 | -48.19287 | 2025-09-09 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 697901a1-bd00-30a8-823a-795023614cf6 | -15.27036 | -52.35999 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fd96951-9645-3e39-a584-c340f385a839 | -12.95067 | -54.80882 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 974441a7-e5bb-302e-ad8b-5869954a475a | -15.25735 | -53.79734 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2b37122-2af1-3995-ba1c-9db64f76b252 | -12.87453 | -62.10838 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9674eae3-ea36-3df7-b74c-b9bd1138a4f6 | -4.27416 | -48.19707 | 2025-09-09 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3823ff70-1047-39c0-b559-0aa456346af9 | -7.40328 | -61.63321 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6225749-4bd6-30b6-b302-0ec69da6c3c7 | -3.03964 | -59.17258 | 2025-09-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b082f911-4ec5-35f2-80e4-c5be2b892214 | -2.51361 | -51.90454 | 2025-09-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e66ccb9-8d07-3ad0-a120-39bd7f6616c0 | -11.81399 | -63.00311 | 2025-09-09 05:23:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22975798-a2de-35d6-ab76-31f6032e9411 | -12.942 | -54.8026 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d794f82b-a37d-3cf6-b7f0-a0048fa72fa2 | -15.50416 | -52.75911 | 2025-09-09 05:23:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6603aab1-6ada-3512-9236-013fdf15e45d | -15.78316 | -53.53449 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5018dc3c-6a21-3268-b185-6965153482bc | -14.73787 | -55.91111 | 2025-09-09 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aec357f1-34a8-3f17-98fd-496ec08966b4 | -16.08153 | -50.49174 | 2025-09-09 05:23:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 271c1a2b-f96b-32f4-90f9-ced1161f3900 | -7.5203 | -61.66629 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 267c2993-1b5e-38d6-94c2-f4fb14624b7a | -8.0158 | -63.48502 | 2025-09-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53deaad9-8904-34a0-be0e-2ccef2f30b48 | -4.90124 | -56.01251 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a6effe7-0253-3739-bafc-504c3b75eed3 | -5.41966 | -51.53497 | 2025-09-09 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40cf0af3-a33a-39db-9fcf-ada43213930f | -15.87156 | -52.20654 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bc9097c-7b1c-375b-a321-4d8c3aa85803 | -12.8784 | -62.10539 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c28fc2-bcf7-3ee6-bea1-a44fae9231cb | -12.84815 | -52.94647 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2fcd2b49-857e-3d09-a603-edaba5200704 | -12.88595 | -47.98468 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6df93557-c418-3836-bd0d-8e464b57650b | -12.89885 | -62.08364 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 512b1373-3d94-3c1c-9e25-d4473dac33ce | -14.7028 | -60.25523 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f8c418d-ceca-3c14-b6be-73eac7b41283 | -11.8892 | -64.9945 | 2025-09-09 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b3c88b6-747c-3d3a-98ed-afcb71229423 | -15.7463 | -53.52928 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2a89808-bf8b-3ab1-9dcb-810ddb767ea8 | -8.01866 | -63.48954 | 2025-09-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3de1141-de94-3fb0-ab89-1f578a9c7415 | -7.52086 | -61.66278 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7b68a86-5ddb-3383-b779-8a276e5a8cba | -15.87412 | -52.34351 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7fa38d6-6f1a-3e86-8571-d6168ce7e2bb | -6.26847 | -52.80365 | 2025-09-09 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4891038f-e0fe-3fcf-a8bf-48a4a7436205 | -4.27637 | -48.19374 | 2025-09-09 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0cb7736-464f-3adb-96b3-50f4198b67c5 | -14.44378 | -53.24142 | 2025-09-09 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02b01825-37ba-3410-82ff-5fabd863b936 | -12.18507 | -53.88213 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a2632d3-0eeb-37e8-ad1b-4a0e3fc0a0f6 | -15.25627 | -53.80674 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7153cc4b-5b2b-3cdc-ba80-261eac6bfa7f | -15.86578 | -52.20604 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08321e41-b630-34e9-bbfe-e1f092ef2619 | -7.34162 | -49.5663 | 2025-09-09 05:23:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39482922-5191-336e-b983-b6a76cbb6d34 | -14.62196 | -52.15855 | 2025-09-09 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 32edcac9-75e5-3721-a77e-73ca52002b68 | -4.27494 | -48.19183 | 2025-09-09 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f29cab15-cae2-3e68-8875-8541a790c1c6 | -15.78395 | -53.52782 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50ea733c-d803-3b98-b53f-83c648e6f698 | -5.42488 | -51.53571 | 2025-09-09 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b47383d1-6cf1-33df-aa45-7f4f32631475 | -15.24194 | -53.77906 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c8c7107-33d7-3097-a741-97de81ac11a0 | -7.5858 | -61.68072 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e459e438-1ffc-3c7a-a08d-42f2414fe78c | -12.84856 | -52.94318 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f212d811-0c59-3d48-8bf4-76c7af932b0d | -15.23891 | -53.77592 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0243c7a-23d3-3380-969a-947dc758a2de | -14.5235 | -48.74599 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26138ab2-8332-3e63-8e6c-697e6421c29b | -15.75682 | -53.53086 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b77837a6-7662-3af4-bafb-8093eb454ae9 | -12.8762 | -62.09779 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e14417d-fd3f-33aa-b44c-c5ef2f0c5a32 | -15.78399 | -53.57268 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e3e69f9-4e9a-3075-86c5-5bc4cb60b514 | -15.2485 | -48.82039 | 2025-09-09 05:23:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d49c9c65-620e-3105-b370-867df14643c4 | -12.87676 | -62.09427 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea1549ca-42c8-3aec-92b4-bec1956676ee | -5.49968 | -60.13888 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e2901bd-758c-3dad-821f-59fa5beeb92e | -12.83562 | -47.97993 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 595b4249-e915-3c73-88e9-79055698d845 | -15.24522 | -53.81189 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b80b1eec-a93f-32a3-8f15-cacb3d890d76 | -14.87232 | -55.80772 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 090919a7-8345-3548-b4cc-6fe004f9244e | -7.95241 | -63.60563 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fab26234-7fb8-3333-b7e8-490f74f199a1 | -8.08687 | -54.75873 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4043c3e4-eaf5-3678-9b63-d48755a60acc | -5.50353 | -60.13595 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d085477b-b916-3e3b-b073-815bfb63dda4 | -15.25772 | -53.7942 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af6ca5b8-e5e8-3ab1-ae7c-f3d81c96d209 | -15.81985 | -52.25485 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 368d7a3c-8677-3f63-810d-b4582fb4f02a | -15.11268 | -52.36103 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bbcf82a2-056b-308f-b42f-5383eb4600b9 | -4.99529 | -56.25829 | 2025-09-09 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README62.md)
