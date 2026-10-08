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

## Dados Diários - Página 222

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae3de9a6-e49f-3ef2-9ff4-254373b6ceb6 | -3.4096 | -57.982 | 2026-10-08 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 33fe490d-bfcc-343b-a8bf-9f04ef0faf16 | -7.8876 | -55.0023 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ae38aa9e-b4d6-3fd9-ab6b-f9a95f952f03 | -2.9264 | -54.1505 | 2026-10-08 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c086488b-816a-3a16-8f7b-a05826912376 | -7.7579 | -54.9499 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ad033b35-8aba-3fd4-b027-b9f57ec185bb | -3.0798 | -58.0276 | 2026-10-08 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 94dfeb36-df7e-347c-9007-c30bafd09832 | -3.3723 | -58.1957 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6c7f9204-d608-3954-8b3d-09194b8ff25f | -11.8508 | -43.5361 | 2026-10-08 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 15bab87d-3bee-3fbd-89e8-665ad80d12b8 | -8.4829 | -62.6927 | 2026-10-08 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2e3698d5-a2bf-3f3d-90d9-3e0abaa8b36e | -3.8155 | -57.1751 | 2026-10-08 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 23497c24-d81b-343f-98ae-82f1fd2b2557 | -2.7332 | -57.6077 | 2026-10-08 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| ec60768c-de7d-38a7-b33e-7e53372f2fd8 | -1.823 | -55.0897 | 2026-10-08 15:20:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| f12e001c-8c7e-3b06-a608-14f51e2d335e | -2.3863 | -57.2247 | 2026-10-08 15:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 4b529739-1e28-3b33-b30c-2ca4af0aab0b | -6.0817 | -53.4881 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 45b80a26-b6b8-319e-b084-178ffdb5b784 | -6.737 | -55.0674 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0f579d4e-de6f-3043-93a6-9da2727b9855 | -1.1094 | -54.1601 | 2026-10-08 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ab7c8a9f-be5f-350a-889e-8a31f86e966f | -3.3358 | -58.1578 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c95eb657-05e4-3d9b-af1f-932101d3553e | -5.6934 | -53.4667 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 0055dd6c-323b-3ef7-9a63-ea7b583961c1 | -3.2451 | -57.8693 | 2026-10-08 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a2b5ce5b-e116-3688-b012-5addc9f533f2 | 0.3772 | -51.1489 | 2026-10-08 15:20:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f5d89186-1e28-3b7f-bccd-3cb0edc3fd89 | -3.4094 | -58.0207 | 2026-10-08 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7d3fe7ae-612b-3852-b527-94784c6860b5 | 1.6568 | -55.7847 | 2026-10-08 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e19fda05-5ec8-3d06-864f-00e0d0703c87 | -2.2222 | -56.9348 | 2026-10-08 15:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 65dbfcd7-6964-3356-bdc8-e437a8580ca1 | -2.6051 | -57.5905 | 2026-10-08 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8573d45c-8560-3547-b71e-b2d943d3faad | -10.9575 | -45.389 | 2026-10-08 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| c5ade6b1-dc89-31e4-ab8a-53738198bf3d | 1.6568 | -55.8242 | 2026-10-08 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| d1e1a8bb-4e84-3533-bed8-531503641ac2 | -3.4095 | -58.0013 | 2026-10-08 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ae9f482d-7b18-3731-80cb-8b6f9b5024a1 | -3.0799 | -58.0083 | 2026-10-08 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 43322366-ec71-3b25-b185-402daca4d6c2 | -1.2082 | -49.2539 | 2026-10-08 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 4f7c6328-4508-37ea-bc0e-ae05d3fc4aa8 | -2.4046 | -57.2244 | 2026-10-08 15:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9f291116-76ff-3c7f-859b-cabcf70fed22 | -5.7116 | -53.5065 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f28c9299-30f5-31b4-a330-0be79f1263ef | -2.0447 | -54.3085 | 2026-10-08 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 49e96731-f36f-3f00-b8b6-1a72915a77d1 | -13.1833 | -54.3158 | 2026-10-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 228.5 |
| d9a23c41-235b-3fbb-bba6-c90e514d51b3 | -5.6932 | -53.487 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 62653248-aa8c-337b-85aa-8d5079848b41 | -3.188 | -58.6241 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 19017def-0c5b-3253-af59-528a617e794c | -9.5003 | -66.8017 | 2026-10-08 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.1 |
| f1a633cd-9ebf-39f8-9bb9-de11cc030a71 | -6.1974 | -52.8295 | 2026-10-08 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 52d0cc30-5ffd-346c-b691-7eab4c7830ea | -8.2247 | -54.7396 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 259d7203-e4e0-33d6-badf-2b30d9268a05 | -11.6382 | -43.6166 | 2026-10-08 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 1ed61357-a7c8-3f90-89e0-efc370a6901e | -11.6374 | -43.664 | 2026-10-08 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| b2715fcc-b814-31ff-bbe9-35c4b82387eb | -2.572 | -56.1842 | 2026-10-08 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 35805754-4788-3efb-a1a6-a2833ad5cea1 | -11.3986 | -47.5635 | 2026-10-08 15:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 32d7f624-3736-3071-8af8-efe6d085026f | -6.2127 | -53.2779 | 2026-10-08 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c5c2edd6-da51-308d-9985-3b382d0bd5c1 | -12.1738 | -44.7517 | 2026-10-08 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| fea51a9c-b6cc-38a2-b0a0-af87e81dee0f | -2.0947 | -56.6239 | 2026-10-08 15:20:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| f17a787a-1c32-365a-904f-43be336f9cc7 | -1.1161 | -49.1913 | 2026-10-08 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a7b96cc9-ec3e-309b-8cc1-0d0fe7c241c7 | -2.204 | -56.9155 | 2026-10-08 15:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 210.6 |
| c192fb57-5d99-36a2-b5b9-d50c132fe982 | -8.9501 | -45.1334 | 2026-10-08 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 276.3 |
| 0661dcc9-9811-38b8-b19d-8174ff166c22 | -13.1639 | -54.3385 | 2026-10-08 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 230.4 |
| 9ad97dd6-a7ad-362a-b94b-c81b0a75dc88 | -3.3172 | -58.2355 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 1cca56ac-40fd-3e6a-b11a-5b3f663d72b1 | -10.9384 | -45.3916 | 2026-10-08 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 366.4 |
| 475b5154-9420-3ad6-bcee-3f05783089d6 | 3.7462 | -51.6224 | 2026-10-08 15:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7b6f03e6-f2c6-3656-8494-e3090b2e0aa7 | -3.0926 | -53.9254 | 2026-10-08 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e6f80791-78b8-3cd0-927e-6d71c07fe9f3 | -2.9337 | -57.9143 | 2026-10-08 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d181a70f-5308-3d98-b759-8d466f3c9796 | -2.8163 | -54.133 | 2026-10-08 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 70b305bb-4c91-3a37-9496-f8e9354ef184 | -2.8531 | -54.1121 | 2026-10-08 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a38c3087-fd8e-3c44-98f8-f6ff99347a97 | -2.572 | -56.1646 | 2026-10-08 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 8d59e1fe-59a0-335c-9bb6-adb7aa4e4899 | -6.876 | -59.34 | 2026-10-08 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a27f8c36-4b7c-3e4d-abf7-dacdd86d082a | -9.1407 | -64.4024 | 2026-10-08 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 24669d56-cc9d-390e-9b51-3adef53b1578 | -2.8433 | -57.4891 | 2026-10-08 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 1d999e10-1e45-354b-ad3a-8f7fbf7f6bbe | 1.6385 | -55.8047 | 2026-10-08 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8aa53f06-f121-358c-b3e0-d2914ddde661 | -6.3217 | -53.5772 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ada71ff4-b07b-36f6-89a2-e49c82702bee | -2.3115 | -57.9829 | 2026-10-08 15:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 98496289-00e3-3cea-82ad-b35f3e38c9f0 | -1.5302 | -54.8151 | 2026-10-08 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| d2430bd6-8987-310f-87b9-f28a6e50eafc | 2.7458 | -60.0109 | 2026-10-08 15:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 1c18c0e3-37da-3c9e-85ce-f74e7c4772cc | 4.2247 | -60.7051 | 2026-10-08 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 4158a062-92bf-3a24-9333-1f7b7e2e8201 | -5.7312 | -41.7309 | 2026-10-08 15:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| e7c70b93-5bcb-3853-83f5-6494e2265064 | -3.9483 | -56.0335 | 2026-10-08 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4b4c4201-15b9-322a-9021-693f6d286d75 | -12.1948 | -44.6554 | 2026-10-08 15:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f3613f95-e422-34d7-bf69-69c17859d9ca | -3.3912 | -58.0017 | 2026-10-08 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 73208ff2-8d73-396e-a99d-8f80a29a8eb8 | -3.0631 | -57.4847 | 2026-10-08 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 45efd69c-282a-392b-91fa-887a67cc3c1a | 1.8222 | -55.5258 | 2026-10-08 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 62dfa0bb-a6ca-3889-8b53-ae41746b4419 | -2.788 | -57.6261 | 2026-10-08 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| aed86acb-b0f6-329a-863e-edbae0b602ca | -3.1114 | -53.7839 | 2026-10-08 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| f4dc4084-173c-3ae3-8343-2eaef0279f64 | -6.7845 | -56.2393 | 2026-10-08 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f2571322-9ea4-3248-9ada-881861e1223f | -2.2223 | -56.9152 | 2026-10-08 15:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 196.3 |
| 7c437889-dcdf-3b26-b7d8-85e268b15e10 | -6.6628 | -55.0912 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 5c77d62c-d85c-317d-a5cc-cc4730f54874 | -12.1742 | -44.7284 | 2026-10-08 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 8339e12f-3c23-34e7-9367-d2c54cef5247 | -1.3277 | -55.4327 | 2026-10-08 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 536914f2-e9d1-35b2-aeda-59b4b116576e | -8.0769 | -45.5886 | 2026-10-08 15:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5c6451cd-0643-35a7-9352-0d41a0561042 | -6.6627 | -55.1112 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 184d063b-7873-3ac0-b30d-4f0b27a55b56 | -3.8786 | -44.1265 | 2026-10-08 15:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| c374c526-3500-3b52-b1f4-e8fe4953c578 | -3.2268 | -57.8696 | 2026-10-08 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fecb391d-b42a-3311-9e1f-e439742a2e7c | -12.232 | -44.7194 | 2026-10-08 15:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 8aa62937-98b8-3afe-aeb0-ed9e8aee3d4a | -3.1633 | -54.7253 | 2026-10-08 15:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 3ac7f969-e8fd-3a8b-93b2-e083040177ee | -3.1697 | -58.6437 | 2026-10-08 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 238.6 |
| 7ec3514f-6d46-30a7-86fd-97dda23da117 | -8.2433 | -54.7384 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 04010410-bc95-3014-a57f-f1bc3426a9bb | -2.2198 | -58.1196 | 2026-10-08 15:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 031f3f60-9469-3dc5-ac3a-a81dfbfefea9 | -2.8434 | -57.4696 | 2026-10-08 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 0172fb1f-901f-3360-9132-c8987fccb192 | -3.0008 | -53.8874 | 2026-10-08 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 66a5baab-a3bb-3b3d-92a9-3e20a4cc718b | -1.5123 | -54.556 | 2026-10-08 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4341f426-71c7-32a3-8580-ff4ac528e4ca | 2.7641 | -60.0106 | 2026-10-08 15:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 657f4e06-e6ce-32d5-813c-f850a893da12 | -2.8347 | -54.1125 | 2026-10-08 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 65147f32-4b7a-3ea1-a35a-a9af000603dd | -2.6079 | -56.4782 | 2026-10-08 15:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 32373089-7ff0-368d-a393-4f3ad97c9857 | -7.89 | -54.7206 | 2026-10-08 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c347e205-4829-34b6-9756-dce6ef7d2f21 | -0.34 | -52.0359 | 2026-10-08 15:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6328e92b-3981-33ec-a02d-abb4d23ce8dd | -6.2159 | -52.8285 | 2026-10-08 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 32f3b585-c1e4-3afe-9207-5d4045fd7360 | -6.0423 | -42.5859 | 2026-10-08 15:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 118f3e5f-6463-3012-9433-2c31a600ad46 | -1.2639 | -49.0618 | 2026-10-08 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ffad7c38-e1a8-39ab-bba4-617d20de37e0 | -1.3934 | -48.9321 | 2026-10-08 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 07310ccf-fd3e-31f6-a255-2347706dfef3 | -2.8346 | -54.1326 | 2026-10-08 15:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |


[Clique aqui para ver as próximas entradas](README223.md)
