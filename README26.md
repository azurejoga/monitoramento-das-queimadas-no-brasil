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
| 2ec2bbc0-6b5f-37e9-ad14-563c069f8b1b | 3.38855 | -61.21103 | 2024-12-11 05:18:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34ec388f-9460-3583-977d-369b8853c2b3 | 2.42819 | -60.65398 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be538d20-9663-3dbf-89d4-dffe0db24080 | 2.75523 | -60.64038 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 92f10818-d540-3f65-af8d-1fe4566dd2b3 | 2.73868 | -60.39512 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a8566368-dce9-3a21-87c9-6e5377387764 | 3.22851 | -61.19985 | 2024-12-11 05:18:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c8295808-2ae9-3c8a-837f-6d0a9b323140 | 1.17116 | -59.22606 | 2024-12-11 05:18:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7dea273-1bcf-32f2-b0c1-e5772137b25d | 2.7564 | -60.64804 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 82428a3c-fd6d-3f7f-b762-b650797101d1 | 2.75234 | -60.64474 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32786247-e32d-397e-8485-f0f9dcfa1b66 | 3.23567 | -61.19875 | 2024-12-11 05:18:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 14f83e68-dd6a-3ed0-bcdd-86ad35ea2507 | 3.20713 | -60.59321 | 2024-12-11 05:18:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fad86a84-cae0-31fa-9529-9193ae536c76 | 1.29631 | -60.42749 | 2024-12-11 05:18:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 371d78e2-3e8c-3029-b617-308fc0d33531 | 2.57429 | -60.6907 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d7641c2-0b5e-3a70-916e-41a9a93efa87 | 2.75059 | -60.63328 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb519e77-c099-3a7b-99d1-5d271d78d99c | 3.23145 | -61.1952 | 2024-12-11 05:18:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 68b588c7-acb4-35d9-85b0-f8f85e1e63ec | 2.76276 | -60.64313 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 348a45c6-5ce7-3752-b9c2-c6747ee69d14 | 2.73926 | -60.39886 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd7ce9ec-e710-328d-99e2-27ac42e0e9d3 | 3.22725 | -61.1917 | 2024-12-11 05:18:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ac51124-2bfe-3c56-8783-5935c3c77c43 | 3.23209 | -61.1993 | 2024-12-11 05:18:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ddf37af6-9bae-3441-8a6e-a33b60f841ee | 1.30092 | -60.40806 | 2024-12-11 05:18:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dbde2e2-48e7-3336-9866-822744133a97 | 2.75464 | -60.63657 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0b30d37c-1acf-34e5-a853-cd04c35876c6 | 2.75293 | -60.64857 | 2024-12-11 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b4a7393-15a9-3882-a023-602bac37db28 | 3.2363 | -61.20283 | 2024-12-11 05:18:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07fc3f3d-ffa6-3c20-866a-b0a04fe14f9e | -6.8972 | -43.4969 | 2024-12-11 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 2d565b11-cf0a-3718-8568-ae2d34e84427 | -6.1368 | -42.5307 | 2024-12-11 05:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| 26ba3135-13a1-3ca1-8766-261c446cfb39 | -6.978 | -42.9977 | 2024-12-11 05:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| dd20806d-5613-3cce-89d5-922c5ca4b9da | 2.7627 | -60.6378 | 2024-12-11 05:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5c543372-4f25-3303-b6d2-1fbc49b41862 | -6.9161 | -43.4952 | 2024-12-11 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ea547221-502b-3da2-b814-6c32533761e9 | -6.9158 | -43.5185 | 2024-12-11 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 645d4401-2050-3d49-a658-ea7b3e951b93 | -6.1178 | -42.5559 | 2024-12-11 05:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| d579f4dd-f8c2-3acb-a1ae-c787a86e02ee | -6.897 | -43.5202 | 2024-12-11 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a8347183-a8ef-3630-9f96-7708746172a3 | -6.1366 | -42.5544 | 2024-12-11 05:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 0f4eff82-310c-3a04-a67c-284433dc3d3e | -6.9592 | -42.9994 | 2024-12-11 05:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 150.7 |
| ffa64c84-dff0-3242-b4c0-58fc0fa98b55 | -3.1288 | -54.0853 | 2024-12-11 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f50db396-e16b-359d-a296-b2dcb12bcdde | -12.6755 | -45.6672 | 2024-12-11 05:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| cf76b899-47c8-348e-b415-a63c47ffa945 | -6.9594 | -42.9759 | 2024-12-11 05:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 95b2ea6f-95bc-35be-aff7-8786a9c1cf6c | -6.118 | -42.5323 | 2024-12-11 05:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 7922a6da-7d1b-3fca-8246-84887b23ca77 | -3.12994 | -54.08855 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0f1c834-3e5d-395b-9ad1-9567c5125587 | -2.56099 | -53.42595 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ed0b2e9-49b4-3b4c-90f9-04251640f6ed | -2.47925 | -54.12744 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a44c6d2-0eb5-3cd6-929d-18d26fb6eb99 | -3.52853 | -53.94008 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c88bcc7-3ae5-36d0-ba4d-c96274e4acc4 | -2.55665 | -53.42537 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d49d7e56-bce4-38c3-abba-08e006363170 | -3.11441 | -54.07835 | 2024-12-11 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f6a21d4-8c4d-392b-8651-d11dd64ab206 | -1.39775 | -55.08089 | 2024-12-11 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a33a7b9f-5b04-3f5a-8391-27cea847a7be | -3.45479 | -54.65763 | 2024-12-11 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b22b684e-1c3f-36d7-9a67-8192ae2262ff | -3.11916 | -54.07523 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4104be54-a3c1-3e4b-875e-beca25429df7 | -2.41718 | -53.68976 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6f866db-940d-3fc4-a181-20f045b0435f | -1.46961 | -55.39623 | 2024-12-11 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a91d6714-833e-3235-8f0b-a2aad99627c1 | -3.45425 | -54.66122 | 2024-12-11 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae2c1ee8-12bb-3803-b637-47272882b294 | -3.09658 | -54.08323 | 2024-12-11 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d11ab97e-3aea-3462-9935-96ff86ec401a | -2.37365 | -53.86196 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14eaf17f-338e-3cd1-b499-cd7521ee301d | -1.84499 | -55.24498 | 2024-12-11 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe1e86cf-63b0-3123-9cae-00b56b11a49b | -3.12519 | -54.09168 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c763ec9a-0d0f-3d9d-b803-a5edc54e3535 | -2.41657 | -53.69371 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 238bb8f8-78bb-32e0-b6c1-efd6876c6bf3 | -3.09184 | -54.08638 | 2024-12-11 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc2c3026-e75c-3d3c-af1e-73f7b9e703b3 | -2.78324 | -53.23638 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff2aace5-511b-3b66-8b91-a675bd165390 | -3.10493 | -54.08453 | 2024-12-11 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58ce0627-c33c-3788-89b6-e8ec62f25763 | -1.6932 | -55.67314 | 2024-12-11 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aed02caf-6669-3be2-bdbc-8951bcf28645 | -3.33567 | -53.24112 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ed350a5-aa76-35b4-82cf-df4f4ea6fc6c | -2.45481 | -53.98233 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 120b89e7-6e05-3e4f-9080-d90c39fe4238 | -2.44865 | -53.71089 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f259c51d-70ec-3ad7-b9be-e5cbf5b17264 | -3.29081 | -54.11515 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d79d1493-aed1-3d22-8fb6-72dc2e4887c1 | -2.25894 | -53.8483 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b0521653-6dfc-3cd4-b330-cd3caff87128 | -2.77822 | -53.23986 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c227702-d43d-3d2f-9cb0-5f03584cc56d | -2.95494 | -53.11522 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e58472a9-2198-376d-876e-5790d5b59853 | -1.46586 | -55.39564 | 2024-12-11 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57420287-f1ed-3be5-be41-3b14d1ed2221 | -2.45348 | -53.7077 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b30701ce-a286-3c95-bfea-d8d957b6c714 | -2.79203 | -53.23786 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10b999cd-51d0-31ba-a6d2-a23ef201e93d | -1.70485 | -52.61091 | 2024-12-11 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6c1024b-68cb-3e55-adb6-be8758bda59e | -3.12799 | -54.04536 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79f03c69-c8be-34a4-9583-cf40ff08649a | -3.12577 | -54.08789 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 550b38f6-339a-39c6-8d42-1ddf967ad6cf | -2.3035 | -54.00215 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f54dcfd-2c8c-3ed7-b9ca-c140ef8177f3 | -1.39703 | -55.08564 | 2024-12-11 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 024c937f-5a90-3c04-beee-066e8d67bebe | -3.12439 | -54.04088 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98d350d2-cde7-3746-9d4a-dba7eb077161 | -2.96479 | -53.7271 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65ff6ce1-6361-36c4-8dc6-f8801bc05940 | -2.45425 | -53.98606 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6eb0e3d-a8de-3ab7-a264-d26734441311 | -3.10967 | -54.08144 | 2024-12-11 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f412b91-4942-3889-963f-cd5396c0c0fa | -3.71448 | -54.2004 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8a95f98-41d3-3294-9b06-8155e6d09fd8 | -1.47031 | -55.39172 | 2024-12-11 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cba0621-73d6-3887-8ed2-ebc69f301cb3 | -2.79642 | -53.23858 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83e231cd-b7aa-3a03-94ce-1a944d1fdf60 | -1.41197 | -55.14099 | 2024-12-11 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eead9f1c-9476-3313-aafa-6d39e879a8e6 | -2.96418 | -53.73107 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38a69846-f731-3780-9540-44d449733e44 | -3.12936 | -54.09236 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02f8bc63-fc2b-3eaf-9129-f9b9db2b8a22 | -2.41174 | -53.69694 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a3d6518-8c52-3c99-99f4-136b7b6e9b3e | -2.96052 | -53.72645 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b53f82d-04d3-3f67-9195-29dfc5033705 | -2.44925 | -53.70702 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47facff0-6dfb-3ff7-9f07-6681040ac2e9 | -3.11024 | -54.07769 | 2024-12-11 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05b4a6f2-1346-3fa0-b596-9b8ea2c07a86 | -3.7139 | -54.20426 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0312b5cc-10fc-3369-af27-8f949f33ee0d | -2.78261 | -53.24058 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26f8c18b-90ab-3aa3-8343-0d1ef8f50da4 | -2.79141 | -53.24198 | 2024-12-11 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08354a7f-39e5-3948-a2ac-602db2cac27b | -2.47982 | -54.12373 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55615d41-23d7-3c26-82e6-53401bf5980c | -1.73801 | -55.55756 | 2024-12-11 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f1bff2-815e-3881-85a3-4e92b332f6b0 | -3.52794 | -53.94409 | 2024-12-11 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03b535d3-42d9-3d27-8829-5a00f78b20dd | -2.09737 | -55.31669 | 2024-12-11 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1261d1d8-5ee2-3152-8228-3dcf4f9ce89b | -3.1091 | -54.0852 | 2024-12-11 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a64d2252-6375-3099-ac97-3694e1e185d6 | -1.47337 | -55.39682 | 2024-12-11 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90f39f33-ca50-34a2-836e-b42a9743e5ac | -2.29616 | -53.91251 | 2024-12-11 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77bedd1b-f4ef-3dd0-8cd3-6f4b9ce8a454 | -12.54282 | -58.36927 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a471657-7b1d-3b98-a086-353571ad568d | -12.5544 | -58.36658 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2cdfe04d-b160-3004-9dab-a934cb0c89b0 | -12.55503 | -58.36226 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8315e70b-4e1e-3db4-8ab4-13985ce8eca3 | -12.5423 | -58.347 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README27.md)
