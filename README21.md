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
| 62858693-96e9-3ab1-916a-fbfb1d113664 | -9.462 | -60.549 | 2025-08-29 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 3e72f702-d030-3298-9900-e2da5693ab32 | -9.7728 | -64.2657 | 2025-08-29 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b654d24c-7bb0-3c74-a3b8-445cf9b95e10 | -3.7693 | -54.8286 | 2025-08-29 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| cac09769-246f-39b6-8ae2-a875f75fbda4 | -6.5546 | -43.9221 | 2025-08-29 03:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c5ff4e95-0ce1-3a92-9ba6-1d81410545b6 | -10.8608 | -60.7998 | 2025-08-29 03:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9a72acc8-2117-3ac4-8079-19fac6cd3014 | -9.7322 | -64.9067 | 2025-08-29 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8fad13d1-cc72-3a25-b65c-b08c04e87089 | -9.4618 | -60.5682 | 2025-08-29 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 2ddf9362-6b18-3dfb-b428-7a437c028301 | -12.4345 | -63.9173 | 2025-08-29 03:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 30942244-3417-331a-815c-2c8c016772d5 | -9.1155 | -65.7699 | 2025-08-29 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 7d596733-5b92-3d6b-9dbd-4ec07856fdf1 | -8.1758 | -61.3755 | 2025-08-29 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 776bb8a6-0a3a-3875-bdae-b6fd3f0f08da | -5.6081 | -45.0038 | 2025-08-29 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ae1d5680-7fe2-327b-a569-d054b6ee6df0 | -9.1525 | -65.7874 | 2025-08-29 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 951b0cd9-0ccd-3b00-bfe8-50717c770c3d | -10.3812 | -57.8245 | 2025-08-29 03:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 051e7c64-433e-325e-9ed2-069ae5f5edc2 | -9.1154 | -65.7886 | 2025-08-29 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d6f8fe89-dd5e-3df4-8516-98efa87b0e6f | -10.3624 | -57.8258 | 2025-08-29 03:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d089d789-dc11-342d-bfbe-6872a0d049ee | -13.1837 | -45.2865 | 2025-08-29 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 9a441d0e-9d6c-31a9-86bf-fb337dfe9dd0 | -13.5386 | -46.8775 | 2025-08-29 03:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0c293048-a6e4-31e3-9ac3-10125200bed0 | -14.7777 | -59.7353 | 2025-08-29 03:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| e8183ff9-6bca-3a1d-8518-fe0625d6bc77 | -6.9867 | -59.3354 | 2025-08-29 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 22e08b0b-0b45-3fc9-80dd-e48f8d7ede9f | -9.0969 | -65.7705 | 2025-08-29 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 5787c3b8-ed9b-363f-9bfb-46dec852d4cc | -9.4432 | -60.5692 | 2025-08-29 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7e4a7580-caaf-3536-9dda-3caf98f787d5 | -9.4433 | -60.5499 | 2025-08-29 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c5fcf1aa-515c-3a69-ae28-3d9411195f80 | -4.15167 | -38.47971 | 2025-08-29 03:23:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9a11339-72e1-3d4d-91df-f494ff35ec73 | -4.15077 | -38.48247 | 2025-08-29 03:23:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a8648124-9f3b-3e87-acdf-d10b39c7904a | -4.15128 | -38.47939 | 2025-08-29 03:23:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 24abde7e-5622-3a56-bb1e-ea16f14934d9 | -5.53442 | -36.84998 | 2025-08-29 03:23:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3fdaf52d-fcca-3c43-8949-080c17473568 | -3.97743 | -43.25025 | 2025-08-29 03:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97f1f9de-7c37-3946-8005-62f4e58fbcf2 | -3.97858 | -43.24362 | 2025-08-29 03:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5a10cbb-384d-3c03-a416-ac7c04666e35 | -3.97422 | -43.25222 | 2025-08-29 03:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e389bd2c-8707-3d5b-b6cd-4ffb63a5167c | -3.9704 | -43.24914 | 2025-08-29 03:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0065d84-ee67-3f78-b2a2-48c48610b64e | -4.15113 | -38.48282 | 2025-08-29 03:23:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 74768676-c924-33ae-ac2c-fc0f74dc9167 | -3.97541 | -43.24559 | 2025-08-29 03:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cca5ada9-52d3-3f13-a3c1-97dcd7bfdb7d | -6.88247 | -43.60585 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87c265d9-92c4-3159-b909-896a42d42801 | -7.41438 | -42.06214 | 2025-08-29 03:25:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c229737d-27b5-3a59-bcd3-6462a6f088ee | -7.64222 | -42.66264 | 2025-08-29 03:25:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 012ad3ce-7c26-3eb1-8fdc-86515f402c05 | -12.35484 | -38.27952 | 2025-08-29 03:25:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 242de368-6ec8-32ad-b33c-5d1477497781 | -4.50572 | -43.69072 | 2025-08-29 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0200218e-0ae3-3160-b04b-7a312cce75f8 | -11.06596 | -44.76463 | 2025-08-29 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 976a624f-5293-36ca-a347-3bff270038b6 | -7.04353 | -44.37045 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b204508-6e96-386e-9549-f3f3438b4cdd | -7.04796 | -44.38622 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 170ba3a6-3026-36eb-83a1-3980d2f1efd8 | -6.49143 | -43.5373 | 2025-08-29 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2128a725-a8a2-364b-8d39-546e6d4133fe | -5.87318 | -42.97045 | 2025-08-29 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 7d45b7ad-60cc-3b07-a113-a453be029dc5 | -6.4383 | -44.57435 | 2025-08-29 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64c92b86-bb5e-339b-a95f-f4b3f1dcf34a | -6.44475 | -44.58048 | 2025-08-29 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a77c07fb-1008-33be-888d-c505182790b4 | -6.88542 | -43.62563 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9a7d763-231f-3524-ac0e-47e3785e7384 | -6.55341 | -43.9239 | 2025-08-29 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8a88d1b-89f2-3bd5-86e3-bc5088328480 | -6.87983 | -43.61771 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ccbd73b-84f1-33f6-a6ac-ef8cd41febe9 | -7.04224 | -44.37733 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f063999-1a49-39f8-a3ee-a03b40eea059 | -6.53538 | -43.10396 | 2025-08-29 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d3776a3-fa05-37de-aa75-e690bb45c9a1 | -6.54531 | -43.92838 | 2025-08-29 03:25:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fde72f8f-f7e4-39d7-9b5b-6eccb0209dd9 | -11.32384 | -43.5656 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a9043dc-83f5-3d34-8a21-e9c4b758bab9 | -7.04443 | -44.38091 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3787d1d1-5e47-3804-a2e5-7e5a2fa172fd | -11.35227 | -43.55566 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08f899b5-a7f3-3e41-b601-2c329cd7a4e4 | -11.28883 | -43.54263 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9395d196-fc77-37b6-8c14-6f7d81ddcb31 | -11.33381 | -43.28905 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed22406a-b422-3536-8e07-729714b8d968 | -5.86647 | -42.96928 | 2025-08-29 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| bac81a7d-b379-334c-af8f-a774dadc11b7 | -5.79753 | -42.57797 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fb807e77-3d1f-3681-9780-110b3e2f0dcc | -11.32281 | -43.57073 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf5155aa-15ee-38d0-a2ec-2cdcbe09fc43 | -5.78524 | -42.57114 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2e3a29b8-c36a-392b-8554-636361e7f160 | -11.33709 | -43.28804 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a05bdb10-284e-39fa-9289-8b44a2e919fb | -11.35009 | -43.53985 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20a8421b-80f4-34f9-81e3-bd7800c4d6e5 | -6.87859 | -43.62422 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68efe894-3db2-31f0-a89d-5a9121dbae34 | -5.80421 | -42.5785 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 029317a8-1363-3e2c-98a8-4c6283ab5901 | -11.35115 | -43.56671 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a08d7918-0a14-3b65-8913-7971e3e852ed | -6.44618 | -44.57312 | 2025-08-29 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adc8c61a-ea58-3927-9b94-257e7c791f3e | -11.35429 | -43.55148 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76bcf83f-2af7-3bcf-a276-c75f8217c734 | -6.87544 | -43.60362 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c316a70-d452-35d8-b525-9b4aa703b641 | -11.57421 | -44.65253 | 2025-08-29 03:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a9ee2ca-f7a8-3829-9139-0bb0c931a467 | -6.83129 | -42.8237 | 2025-08-29 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 58e19725-c3cd-3827-9221-7726f9fae9b6 | -7.04712 | -44.36706 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1b533b57-ce8c-3146-96d5-d2ee2ea6a4e7 | -7.04618 | -44.35638 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a09be83-1960-3b8d-b54e-5618c26cf2bb | -11.02848 | -45.07438 | 2025-08-29 03:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0393f076-81d7-36c3-97d2-61c0464fe5df | -6.43094 | -44.57342 | 2025-08-29 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b9d11c4-9ee4-3a6f-8594-93c625cba06a | -11.30788 | -43.54646 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a72c0a07-3f6a-38f2-8521-e5f2eea48136 | -6.54207 | -43.10522 | 2025-08-29 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78203e60-2c84-3367-af9e-f73ead692fc0 | -4.51288 | -43.69187 | 2025-08-29 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f5ea635-50b2-3611-b653-bf5a42dd024c | -6.43691 | -44.5817 | 2025-08-29 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54dd1c28-0530-3fd5-8ade-bd1ab9640b7c | -11.32813 | -43.5772 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30f61bb8-f5cf-3fec-951e-d6b4264c2bb9 | -5.86662 | -38.28561 | 2025-08-29 03:25:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 69d7c830-707c-3eef-b41e-0d2432d549ac | -6.54446 | -43.10511 | 2025-08-29 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a118a61d-c741-3213-bbae-53e03bcf4db5 | -9.6024 | -40.35559 | 2025-08-29 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5acd12a3-7e6f-30e2-ba5d-8c1ab59c5a02 | -11.0673 | -44.75812 | 2025-08-29 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3e85efd-81f5-3539-a415-d1757c38796f | -11.35025 | -43.56578 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad157637-a395-3cc2-8a4e-7a39f4861dc4 | -5.78559 | -42.60582 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7a1f69eb-8b74-39b6-8b40-a3ba1e43d4e0 | -7.05312 | -44.35874 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4e615ef-3433-3c7e-abb5-cabc41515b86 | -7.05048 | -44.37278 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c01553ad-a7ea-3ad1-838e-08cf5d27458d | -5.79984 | -42.57785 | 2025-08-29 03:25:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 893d55e9-bc71-3a7e-9874-839a453f5d8d | -11.5006 | -41.52138 | 2025-08-29 03:25:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1544e3ec-c460-3114-847b-43073fa0a79e | -11.34924 | -43.57083 | 2025-08-29 03:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0443f7a9-74f6-3607-a724-876d2b5a01f7 | -9.86563 | -44.69035 | 2025-08-29 03:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f11de2e-291c-3bb2-a7be-823fcb26af06 | -7.0554 | -44.36248 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fbd4f25-9ea4-303f-9f7c-43a5aed62d2e | -7.04922 | -44.37949 | 2025-08-29 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54a95a6f-784e-3173-adc5-6c8056dc1277 | -6.2629 | -43.81141 | 2025-08-29 03:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5edf61f9-afd8-3376-bbb0-cfacfc69e09e | -6.88692 | -43.62016 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5353956-ec8f-336b-b72d-3fcbb646c357 | -4.50851 | -43.68895 | 2025-08-29 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fe36f6d-1683-304f-bda9-6d71fac4539a | -4.50979 | -43.68201 | 2025-08-29 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4923fdb4-3d82-328b-be42-edd666a26d5a | -5.87426 | -42.96457 | 2025-08-29 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| d2e1c1a8-b4b6-3b38-bc69-d5313da20d68 | -6.88007 | -43.61884 | 2025-08-29 03:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ce99081-373a-3628-b7ec-7d2cb6f876bf | -7.6304 | -42.72551 | 2025-08-29 03:25:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 219501f6-4b73-31d3-acf4-17b3d62f1d63 | -7.39919 | -43.38414 | 2025-08-29 03:25:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
