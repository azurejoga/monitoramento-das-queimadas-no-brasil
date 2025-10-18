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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a47f53ea-9317-323b-8869-f8089bae2529 | -9.55978 | -47.7793 | 2025-10-18 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5a362dd8-3070-34dd-9607-7bd35a18bb81 | -14.38766 | -47.89359 | 2025-10-18 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f5acc218-a893-3222-94c7-5ba7498cab57 | -10.74652 | -47.29163 | 2025-10-18 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7f02f1cf-bb1e-363c-8bbf-39d90759d94f | -9.81944 | -47.75664 | 2025-10-18 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 718f8610-9bf5-3e87-a07d-43f376996c64 | -10.95485 | -45.4581 | 2025-10-18 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 263.0 |
| 5b051f4d-b669-3740-b6af-b5ddfe53c481 | -10.33534 | -47.7681 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| db3a093d-b0a6-3bff-8543-75026c2d7a3e | -13.22367 | -43.95644 | 2025-10-18 00:52:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| be610741-7462-3612-90a4-c24eae53d406 | -8.82306 | -50.05059 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c4f2ab1c-d270-3799-a755-5845664eeaf8 | -10.49297 | -43.43425 | 2025-10-18 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 592.6 |
| 5f015edd-e6ff-32a7-a963-ad08033d1a18 | -9.61823 | -49.68061 | 2025-10-18 00:52:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9e701581-b3f4-3ac5-8cb7-aa0e2f253283 | -10.61672 | -47.38625 | 2025-10-18 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bacfacc9-78e9-3c37-8742-972b27a219e4 | -12.9488 | -47.33084 | 2025-10-18 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a55b99be-a25d-3529-8dcd-8717148ef016 | -12.21217 | -43.5721 | 2025-10-18 00:52:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 2289d8bc-62df-3e0f-9bf4-ade8f2ed4315 | -10.49547 | -43.42751 | 2025-10-18 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 469.0 |
| e7812528-f61e-3b0c-a278-c5bc2a6e6a1c | -11.36741 | -45.26954 | 2025-10-18 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 675ac6db-9685-33b2-b30a-71b0176c2b63 | -11.56619 | -48.56452 | 2025-10-18 00:52:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4868648c-15ea-3b99-9c1e-c83f707d5b33 | -8.3897 | -46.24593 | 2025-10-18 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 50ec6c20-0df1-3a67-ab60-b862b6d61893 | -11.48324 | -44.01629 | 2025-10-18 00:52:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| e3a29865-6162-3377-afeb-6dfc61b6677d | -10.71107 | -44.56497 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| dc4f6405-ef8b-35ad-967e-2abe37092660 | -10.15494 | -44.53153 | 2025-10-18 00:52:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 073827c1-f82f-34c3-bb29-a3a370fcf7f2 | -11.59133 | -44.0665 | 2025-10-18 00:52:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5a36bc0e-694a-3989-a13f-866c973e1c15 | -8.88191 | -47.97065 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 425a37d7-1203-3d73-844e-741ab3ea9029 | -14.27515 | -51.8647 | 2025-10-18 00:52:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| dd16d3cd-bc34-39ea-b4d6-689812f59a39 | -13.22937 | -43.98901 | 2025-10-18 00:52:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 895befb0-dac7-385b-ab69-cce9f2b9ce0c | -8.78429 | -47.93586 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 1aac8d2c-e07a-3daf-9538-64b4174ddeed | -13.44629 | -47.9244 | 2025-10-18 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| d3f5a960-2e89-3525-ad44-4beda72538ed | -9.67004 | -48.52905 | 2025-10-18 00:52:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 14754589-213b-34a9-93c9-08e9881d09ed | -9.91314 | -47.67028 | 2025-10-18 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 0329a74d-d262-34ec-86b3-3704725aa43c | -14.33101 | -53.78913 | 2025-10-18 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8a92a5cb-5bc7-32bc-b70c-58541a5cd1da | -9.75581 | -43.93976 | 2025-10-18 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 06dd5ced-eae0-34d3-b7f5-72113a689722 | -14.32977 | -53.7799 | 2025-10-18 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1dfe3789-9a63-38a8-9af1-b19fb2a8e6dc | -15.96385 | -52.13657 | 2025-10-18 00:52:00 | TERRA_M-M | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c38497cc-2bd5-3b68-abe5-246e4277019d | -8.54961 | -50.07169 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cf4f1383-8060-37e5-b76c-08bcfb9a6b57 | -10.92152 | -47.98088 | 2025-10-18 00:52:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6fb7eeb5-95d0-318d-ab16-295746f0de80 | -8.35676 | -46.22482 | 2025-10-18 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a77e77c1-dff7-3750-bfcc-9d6e73685d4a | -13.40827 | -47.97019 | 2025-10-18 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9494e387-5b04-304d-8fd2-a49d8a80f80c | -14.06052 | -50.04804 | 2025-10-18 00:52:00 | TERRA_M-M | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f0f9a060-a296-3d53-ac87-4aebb11c93a9 | -5.25379 | -50.90464 | 2025-10-18 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 68939927-e796-3b09-b464-62b688b72434 | -2.00198 | -56.58257 | 2025-10-18 00:54:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 138d231b-ba51-3865-84ff-d89ff89b0ef8 | -3.80541 | -51.63863 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 58a0fef3-10df-3d21-a0e1-f7f76028f2f4 | -4.00528 | -45.52142 | 2025-10-18 00:54:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 174a90f8-fff0-3f13-9f28-6e766f8a5452 | -7.35282 | -43.86311 | 2025-10-18 00:54:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 1d5d0d21-df28-3eab-8a9b-f1bf3d66eeed | -7.01717 | -55.26559 | 2025-10-18 00:54:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d1b1e8a-ac2d-3d07-99f4-387e1f2bef3e | -2.5682 | -49.10788 | 2025-10-18 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 74062d90-0894-3ed3-957c-70716fdd68d0 | -5.63037 | -50.03481 | 2025-10-18 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f9d744a8-a843-3e7d-8e1e-e9ff91548d0b | -3.80714 | -51.65063 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 072d41c3-54cb-3596-8cfe-476fc9f9d468 | -2.91507 | -52.73095 | 2025-10-18 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 9fdf681d-4624-3cee-8d53-ecbe5f74c028 | -4.53699 | -48.40792 | 2025-10-18 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 255179d0-6950-3b68-b2a2-4f230b6c042f | -4.93484 | -49.76262 | 2025-10-18 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| b5b3ff0d-0143-374f-9304-86dc3c7738ad | -1.98932 | -56.55672 | 2025-10-18 00:54:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab30fd92-3e39-383a-968d-2d5e9cf4d12c | -4.76929 | -46.62238 | 2025-10-18 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 3a21ace6-8055-356b-805d-aad410151e67 | -6.36096 | -58.20747 | 2025-10-18 00:54:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4919ae3c-973e-3ac7-ac19-0a2924deb4f6 | -2.90546 | -52.73226 | 2025-10-18 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 293a080f-d34f-3284-a5dd-14b75216c4b0 | -3.75384 | -49.04191 | 2025-10-18 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 44b1ef59-e896-38b3-926a-320849db3da3 | -8.10696 | -55.08509 | 2025-10-18 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f354a040-eef6-39be-97ac-1ff980f7cc8a | -1.93774 | -56.65321 | 2025-10-18 00:54:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2ca56fc7-feb4-3400-8ad5-ec9d9cd9afd5 | -4.78775 | -45.31445 | 2025-10-18 00:54:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| b0e8e73c-5b62-374c-8fc8-5586035acf84 | -8.33848 | -49.96706 | 2025-10-18 00:54:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d3c2a31f-581f-30fd-9d20-b1e518d7839f | -2.92108 | -49.18852 | 2025-10-18 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 405b5f7a-64f2-3b66-8da8-7fc7c7200384 | -4.0125 | -49.02982 | 2025-10-18 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2fc7be7e-8e02-301b-a7b2-96789a82f24e | -2.1173 | -56.88654 | 2025-10-18 00:54:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7980525c-aa5d-3c96-b08f-d03b1d67e7f0 | -3.78375 | -51.76884 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 2948e825-5d2c-32f2-92ed-4cfc1a597557 | -3.57574 | -49.43951 | 2025-10-18 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 56f62bf5-d702-3ff1-88a0-faf3cfd9dba0 | -3.25361 | -45.97614 | 2025-10-18 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 0db0c26c-91cb-3359-8778-47eda543cb78 | -5.33133 | -50.99691 | 2025-10-18 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 99aece7a-391d-3f96-bc02-42bd05e73bac | -1.37999 | -55.35028 | 2025-10-18 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc28d428-cd78-3755-8496-9794d26baca3 | -2.91834 | -49.16965 | 2025-10-18 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 6aa3c7c5-b8a0-3647-8537-51b99ca248f7 | -3.74978 | -49.0291 | 2025-10-18 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 3c67d5ec-953c-3054-92c7-682c18966b8c | -1.42871 | -60.39859 | 2025-10-18 00:54:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9b80d300-8967-3ac1-8ca6-eeae51f20620 | -3.24594 | -45.98417 | 2025-10-18 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 71df39c4-52b7-3794-9b96-9217785cb8e3 | -2.57117 | -49.12083 | 2025-10-18 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 19646e3c-e394-3dae-9a06-561b40dcb2de | -7.80105 | -54.93617 | 2025-10-18 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c77a7e3c-b9fa-3e1d-a4aa-9beb21e8c0ac | -5.01215 | -46.01977 | 2025-10-18 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 334.4 |
| a5b03857-d4a7-3ddd-883a-6f40d5b68e21 | -2.9136 | -52.72034 | 2025-10-18 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f31f6e7d-0697-39ac-b1cd-4e1a87296a53 | -5.17207 | -48.61324 | 2025-10-18 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 08a42d8e-acde-3376-b695-a8cddefeb636 | -1.9467 | -56.65199 | 2025-10-18 00:54:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 9623821d-884a-3f55-a783-9d3cf138f8d5 | -3.814 | -51.69813 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 96f41850-29dd-3238-bf9a-aaa18bf6c2c7 | -3.79225 | -51.7617 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3dc4c7da-6d03-3a1a-8d0a-f585f4b9b294 | -3.79697 | -51.65214 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a05e934-7be5-320d-99ed-a441bc0dd02f | -3.7525 | -49.0479 | 2025-10-18 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| d4e202d1-ad42-340a-967a-549f6cf94c5c | -5.01689 | -46.05045 | 2025-10-18 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| aa78dd84-071b-3094-aafd-0cd9ea522b46 | -6.89273 | -45.45747 | 2025-10-18 00:54:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a9c60709-4c64-3157-ab4e-e963e940f498 | -3.59283 | -45.9744 | 2025-10-18 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| f5ac8dbf-a535-30f6-b1dd-510bcc9216dc | -6.76342 | -56.85575 | 2025-10-18 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 95481aca-7c07-39ce-95fc-e1b4d8106945 | -3.99923 | -45.52758 | 2025-10-18 00:54:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 91e5b100-89ef-3ceb-b8dd-32d96a54ac84 | -5.88514 | -44.71144 | 2025-10-18 00:54:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b06f7313-ac5f-3387-99b0-1c87c1639953 | -5.92722 | -45.44109 | 2025-10-18 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 4241dcc1-6010-3385-b504-8ffc391fcbaa | -6.53521 | -55.04577 | 2025-10-18 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9af70916-aadc-33a7-9e47-f97bbfbf9860 | -5.10352 | -56.15734 | 2025-10-18 00:54:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9ce08aa2-ca82-30e7-98ed-b84a9c3a6c1c | -7.35259 | -43.86786 | 2025-10-18 00:54:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| aabca6da-6f68-3765-aa6d-b5623ce62c46 | -3.99976 | -45.4857 | 2025-10-18 00:54:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 9ca377d3-2ae6-3210-868e-b781c3d4bb9f | -2.95511 | -49.33562 | 2025-10-18 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| fc8bf5e3-8013-3cfb-b451-0a8cc9381a0b | -7.33522 | -43.86554 | 2025-10-18 00:54:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 7e5f5e95-120c-309e-babe-e3ad89322839 | -7.87054 | -55.37722 | 2025-10-18 00:54:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a6eb5d7-b8e2-3823-b76f-c5771d55df68 | -2.74249 | -49.39764 | 2025-10-18 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 052c59d8-81e3-383f-9582-92898faff40b | -5.44882 | -45.41028 | 2025-10-18 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| bda751e9-cba7-3f7a-986a-402bc469efd9 | -3.79385 | -51.76741 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| bfdf1dd2-9e93-3853-b279-4039f219b0f1 | -6.68012 | -58.74764 | 2025-10-18 00:54:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 137debbd-fa1f-3745-86e6-d0d4dde299f7 | -4.53414 | -44.81863 | 2025-10-18 00:54:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b709e22e-ce33-309b-9cd2-e967ce1b41ae | -5.16908 | -48.59389 | 2025-10-18 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |


[Clique aqui para ver as próximas entradas](README6.md)
