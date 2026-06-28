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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d502fe58-7f2d-3955-85eb-375bc4375fdf | -10.313 | -57.1169 | 2026-06-28 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 48122991-e9d1-3070-b7e6-e65e1dc3dd9a | -12.4462 | -58.5023 | 2026-06-28 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| dff66e3a-e4ed-339f-909b-969334657339 | -11.5241 | -54.8076 | 2026-06-28 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bcc4bed9-d7c7-3fc7-a2b3-f704c9574dd3 | -12.0923 | -51.9966 | 2026-06-28 00:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 33334107-8541-3c7b-864b-0af835637b26 | -12.6048 | -57.8743 | 2026-06-28 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 60b3c5d6-7073-3bca-95cb-940d2fdcafe4 | -12.0917 | -52.0387 | 2026-06-28 00:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| adc2a080-2384-3561-b596-7b16080a464f | -12.1775 | -57.1319 | 2026-06-28 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 85f5124b-1423-3f1e-bd83-d67fc38fb938 | -11.5243 | -54.7872 | 2026-06-28 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| fc62d43a-4662-312b-a06e-739b9ed87b9d | -12.2412 | -56.545 | 2026-06-28 00:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f4aeddb5-c0d2-3529-9027-ac85ea24c07c | -11.2277 | -54.3241 | 2026-06-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 915d075f-f763-38d2-b644-b3e00cb8be48 | -12.6046 | -57.8942 | 2026-06-28 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| b4f59abd-9fc6-327a-89fd-2667a4417201 | -12.1773 | -57.1519 | 2026-06-28 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0fbf3c59-dd67-3e80-a2ed-927b3d665ae4 | -12.4651 | -58.5009 | 2026-06-28 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 85da2b9b-1555-3198-8362-f7d3b5b6dfaa | -13.2963 | -43.5543 | 2026-06-28 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9f40ac31-a849-34b1-b018-4f427684237f | -11.2088 | -54.3258 | 2026-06-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 84c4e8b6-6a4d-3712-8f3a-fd70c23ae8c4 | -12.5858 | -57.8759 | 2026-06-28 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| e01ff370-c683-30b0-8b44-bda8b798ced4 | -12.4654 | -58.481 | 2026-06-28 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 90de5e05-bc6f-3e14-b1bc-56164addb0f7 | -9.0796 | -59.4098 | 2026-06-28 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 928d01d2-ee83-3906-b20b-94b492437438 | -12.2222 | -56.5467 | 2026-06-28 00:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| af32970b-d17e-3d95-9ccc-c3c57e946191 | -11.209 | -54.3053 | 2026-06-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.1 |
| 1023dde2-814f-3d0a-a783-852e41c59214 | -9.0982 | -59.4088 | 2026-06-28 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 95c005ad-c58e-340d-8526-c31c44511602 | -12.1585 | -57.1335 | 2026-06-28 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6d2a3f7e-35cf-3896-8a7a-b901c4478dd1 | -18.4795 | -54.1105 | 2026-06-28 00:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 73.2 |
| a505c275-0898-3904-b8e7-a0fb60cfb050 | -12.092 | -52.0176 | 2026-06-28 00:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 362.8 |
| f9ddc0bd-3388-394b-b8ad-91156d692bd1 | -10.3128 | -57.1367 | 2026-06-28 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| df40886d-43c0-3f57-9396-470f2ffa4874 | -10.2941 | -57.138 | 2026-06-28 00:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 8a22b25d-ca59-3b93-b088-2c68866576ac | -11.2093 | -54.2848 | 2026-06-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 88a2a09b-83b6-3137-a5fb-10bd14144891 | -10.2942 | -57.1182 | 2026-06-28 00:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 198.0 |
| ea200806-75bd-3ff8-b601-217d1d9dd712 | -11.2279 | -54.3036 | 2026-06-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 3898af3b-302b-3095-bfbe-b4dabc9ad51d | -12.073 | -52.0197 | 2026-06-28 00:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| b6c78b77-042f-3681-9ba0-a75af884354e | -11.6657 | -57.2536 | 2026-06-28 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 3ad42dad-f0b5-3ad8-b472-ea72ff37adb4 | -11.5243 | -54.7872 | 2026-06-28 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| b879b323-bd78-3136-81c9-005373678fbf | -12.1773 | -57.1519 | 2026-06-28 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 26aaaf0d-1000-396e-b162-954cf85e3dda | -13.2963 | -43.5543 | 2026-06-28 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4a729d60-deb7-37af-8322-7e3953d026ba | -10.2942 | -57.1182 | 2026-06-28 00:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 186.7 |
| ff04e0ec-df7f-34e2-bdf2-1d08a89523f5 | -10.313 | -57.1169 | 2026-06-28 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| e38a118a-0224-3bb6-a84e-ebf29d172ca2 | -12.0917 | -52.0387 | 2026-06-28 00:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| cf036ae1-a77a-335a-ac3b-a5c9f100354a | -9.0982 | -59.4088 | 2026-06-28 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 3d1c5936-b096-307d-9a22-99904e344b49 | -9.0796 | -59.4098 | 2026-06-28 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| b4369946-c253-3325-b399-1ef2bb86f893 | -12.4462 | -58.5023 | 2026-06-28 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 19ce7882-7643-33c6-b5f2-dbda97e307ae | -11.6657 | -57.2536 | 2026-06-28 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 5c957e19-6e21-300a-a82e-cb5a77a455b9 | -18.4795 | -54.1105 | 2026-06-28 00:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0507e633-9715-32ef-bb12-41286fd2bf28 | -12.2412 | -56.545 | 2026-06-28 00:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 9eb48dc1-b51f-3a09-b759-ae6eda0867d9 | -12.6048 | -57.8743 | 2026-06-28 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 9ae381fa-5bdf-345e-b161-939e4670d32b | -12.0923 | -51.9966 | 2026-06-28 00:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 16d7fd4c-6b6d-334b-a250-934edb2afff2 | -11.5241 | -54.8076 | 2026-06-28 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c230e55d-972a-3165-859f-7fe0be7a50f1 | -12.1585 | -57.1335 | 2026-06-28 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0863eeec-2b1e-3457-b763-010748d850b6 | -12.4654 | -58.481 | 2026-06-28 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| c9df8fe7-cccb-3079-a47e-f3a496913a79 | -10.3128 | -57.1367 | 2026-06-28 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 86dfa616-94e4-3a57-b454-734ece80b49d | -12.4651 | -58.5009 | 2026-06-28 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| edcfe3b5-9633-3a5f-85f1-e9a36488407c | -12.6046 | -57.8942 | 2026-06-28 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 9f82e365-ef91-300b-9ad4-fd7bb4cd6fe9 | -10.2941 | -57.138 | 2026-06-28 00:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 157.6 |
| dd8f1618-b960-352a-9239-31afbd4c27dd | -12.0733 | -51.9987 | 2026-06-28 00:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 0b8b7c6a-5dc0-3e8b-bba1-d99892f92518 | -12.073 | -52.0197 | 2026-06-28 00:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| d4064fb4-f239-3062-84b6-411701440050 | -12.092 | -52.0176 | 2026-06-28 00:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 373.5 |
| c03db611-1b28-3202-8392-eaeb892a76be | -12.1775 | -57.1319 | 2026-06-28 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 1348a9f3-e2ca-394e-b556-04cb725414e5 | -12.5858 | -57.8759 | 2026-06-28 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 15c57509-ed42-32c2-b8c7-2159235a909d | -12.5858 | -57.8759 | 2026-06-28 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 654ea787-ef70-3eed-a5c8-67b1cbe25032 | -12.0733 | -51.9987 | 2026-06-28 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 38fc1a02-52f8-37ad-b4ca-8e074ddf88e6 | -12.2412 | -56.545 | 2026-06-28 00:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 8ce56295-5d45-34f1-9dac-10e1489941c9 | -10.3128 | -57.1367 | 2026-06-28 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 442b5dbe-271c-3c50-9004-b1b7b311f11c | -12.2222 | -56.5467 | 2026-06-28 00:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 24af0b63-4517-3be1-afbb-cc1115b41b34 | -12.092 | -52.0176 | 2026-06-28 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 370.9 |
| 6c38e3f8-9df3-3bed-956e-8fdecd869478 | -12.4654 | -58.481 | 2026-06-28 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 3cb67971-b448-3a1f-afcf-e9a8cd829c9c | -12.0923 | -51.9966 | 2026-06-28 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 0d39a05a-7666-332e-b0c8-9621a67fbcdd | -10.2942 | -57.1182 | 2026-06-28 00:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| e0330247-1dac-3036-9de1-3d9ba3cd4449 | -10.313 | -57.1169 | 2026-06-28 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| d11eeeee-a1a2-332e-980c-4428e2f2510a | -11.209 | -54.3053 | 2026-06-28 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 17c8807c-2bba-386a-8501-f3e3c8b9412e | -12.6048 | -57.8743 | 2026-06-28 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 143.9 |
| ef79cb30-cde6-353f-b4af-e36dea56997a | -18.48 | -54.0891 | 2026-06-28 00:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 50466a7c-2520-3fa4-b6d1-f41238abade2 | -10.2941 | -57.138 | 2026-06-28 00:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 4bd2911a-dba1-3d98-827b-697a34134e9b | -12.6046 | -57.8942 | 2026-06-28 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| a4278035-8dd6-391e-8033-945f719b365c | -9.0982 | -59.4088 | 2026-06-28 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 16a0f00a-9915-3b29-b99f-ec44ab8745d2 | -12.1773 | -57.1519 | 2026-06-28 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 700b283a-11ca-3f0d-aee2-00e6146d2355 | -18.4795 | -54.1105 | 2026-06-28 00:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 2f965819-8e52-3d15-87af-c49c0bfb7936 | -12.073 | -52.0197 | 2026-06-28 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 0f17b971-b1f7-3ed0-a339-bf20eab02382 | -12.1775 | -57.1319 | 2026-06-28 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 6c38c9f0-cdbf-31c5-870c-a28e48a78820 | -11.6657 | -57.2536 | 2026-06-28 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 42c29b42-14e2-3f44-bc84-6fdd63b17fc9 | -12.0917 | -52.0387 | 2026-06-28 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5b3ee64f-7f78-37b8-bd6a-7ffc765303ae | -12.4651 | -58.5009 | 2026-06-28 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| ab42f7bc-3f0f-331c-8d59-a4ff915b7eea | -9.0796 | -59.4098 | 2026-06-28 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d0262f2d-adac-3979-8490-ac8c09933fae | -11.5243 | -54.7872 | 2026-06-28 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 3e2af21b-d1b0-3680-b144-6d388882e691 | -11.6655 | -57.2736 | 2026-06-28 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5ec9f0e8-e416-3516-8ce0-204ed07569ae | -12.1111 | -52.0155 | 2026-06-28 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 2f115d28-1f2c-3d68-8580-706b41f5013b | -12.1585 | -57.1335 | 2026-06-28 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8c2ab724-1e90-3a28-9e58-19fb0b863a75 | -11.6655 | -57.2736 | 2026-06-28 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 3c62df3c-aee1-3e50-aa53-671c451e447e | -12.1585 | -57.1335 | 2026-06-28 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 283c16fd-7ee0-3253-8dec-ae90995271a0 | -9.0982 | -59.4088 | 2026-06-28 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 206777c4-426e-3854-baa1-abe33685e726 | -12.1773 | -57.1519 | 2026-06-28 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 47120202-2f3d-3b88-96b2-863867533fc7 | -9.0796 | -59.4098 | 2026-06-28 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 73030e83-5dc8-3eb7-b7c4-dfad5fda96f3 | -10.313 | -57.1169 | 2026-06-28 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ee4da5a3-acaf-3c20-8970-ccfb2ed5e68d | -12.6048 | -57.8743 | 2026-06-28 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| d294d3b2-1c3c-32d4-9374-5f420c37a5d1 | -12.0733 | -51.9987 | 2026-06-28 00:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3411dea6-1d91-3b94-b4bd-d55273427539 | -11.6657 | -57.2536 | 2026-06-28 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 7c2d7a04-c7be-38d2-a377-42928099996c | -12.1775 | -57.1319 | 2026-06-28 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a4ac2aa9-fea9-392c-b709-181a3084a0d4 | -10.2942 | -57.1182 | 2026-06-28 00:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 0b7299f4-a265-3a0d-b08b-d5ebcc2cd6ae | -10.2941 | -57.138 | 2026-06-28 00:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 137.8 |
| b14c607f-e0a3-3f5e-8be7-d133983280a2 | -12.1111 | -52.0155 | 2026-06-28 00:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| d4bd9071-4306-3565-bb00-1abb4c4533fe | -12.6046 | -57.8942 | 2026-06-28 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1db23fee-23b5-3dcc-90b5-0c7f9fcb6dc7 | -18.4795 | -54.1105 | 2026-06-28 00:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |


[Clique aqui para ver as próximas entradas](README2.md)
