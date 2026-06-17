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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e6cd3e6-1ebd-3d4a-896a-8cae146b0bb8 | -12.1952 | -52.7821 | 2026-06-17 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 4aca3f1a-4447-39d5-8aa8-0b5b6522e9bc | -12.8548 | -44.3625 | 2026-06-17 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1b96ef8d-09c8-33a0-9ab6-4d5fd20c3fda | -12.20867 | -52.7822 | 2026-06-17 12:32:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| b916b082-f51d-360e-98f3-1f3ecfeb630d | -11.59606 | -55.34083 | 2026-06-17 12:32:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 453b7f9c-4408-3256-aea9-3253bf4705e5 | -11.8064 | -58.16048 | 2026-06-17 12:32:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d8fd6a4-57b2-3470-8560-7e96555d30c1 | -12.08249 | -54.61049 | 2026-06-17 12:32:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| dfdbb4e9-72f6-3141-912c-9fe4d3fba96c | -12.2196 | -52.78362 | 2026-06-17 12:32:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a2db389c-2dd7-3c05-a086-1f3f47447cec | -12.29627 | -57.39189 | 2026-06-17 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 135a63bf-e59b-3a06-b661-a562b53e93b7 | -15.53067 | -57.9985 | 2026-06-17 12:32:00 | TERRA_M-T | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 51cee754-7c82-38ce-83b9-dd923289f944 | -11.58687 | -55.33958 | 2026-06-17 12:32:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c2b4647c-b1a7-39b9-a3ba-680443b411a0 | -11.51461 | -56.12789 | 2026-06-17 12:32:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b285ab6d-d364-34bc-90d3-7357765e4074 | -12.55255 | -57.20397 | 2026-06-17 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2ad2ad9c-a6d5-3039-a5ae-024c02128e06 | -12.54502 | -57.19374 | 2026-06-17 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 47331854-4db6-3fdd-9ce6-356a35609081 | -12.54375 | -57.2027 | 2026-06-17 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| fa4560ca-9b66-3f2c-ad76-72c6639c31da | -12.55383 | -57.19501 | 2026-06-17 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a64b74f5-5663-325b-98c4-ee0e11a15667 | -11.4438 | -55.10689 | 2026-06-17 12:32:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ffc0bb5-e519-3689-a247-004d7faaee6c | -12.08394 | -54.5997 | 2026-06-17 12:32:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 39b6b435-2377-3b77-86eb-784a1dc23d39 | -11.5159 | -56.1187 | 2026-06-17 12:32:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 959e9798-6efa-327f-9e5a-e21fb72c4df5 | -11.8087 | -56.99255 | 2026-06-17 12:32:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 26d14e7a-e926-3f8c-a2b4-6539279fc5f2 | -15.0748 | -55.8166 | 2026-06-17 12:32:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6a32b528-6c9b-36d9-b63c-f71445ab383e | -12.54199 | -54.61481 | 2026-06-17 12:32:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ffd8153b-6b2a-34f8-b4f2-03a284776912 | -11.54623 | -52.7691 | 2026-06-17 12:32:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| d6270efb-7cee-3cf6-a7ad-cabf16e88f2e | -12.19774 | -52.78077 | 2026-06-17 12:32:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| c0ceb29e-1410-30d9-99f5-772aee2708bc | -12.20688 | -52.79638 | 2026-06-17 12:32:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 46cbb79a-7b8e-346f-ac4e-2e2b22c1176a | -12.92155 | -54.22198 | 2026-06-17 12:32:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| eb5e91e5-0ff9-3cf9-8e6c-5cc78aef0bf4 | -11.54448 | -52.78298 | 2026-06-17 12:32:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e984398d-4d08-3fbb-87b4-0f992c17011b | -26.86696 | -50.67942 | 2026-06-17 12:34:00 | TERRA_M-T | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| 00f6b17b-9953-3ff4-bd4e-c733ba444263 | -10.1493 | -56.6115 | 2026-06-17 12:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| c96b84c4-caf7-3cbe-a7a3-8f171a790901 | -12.8548 | -44.3625 | 2026-06-17 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f234b14a-6f25-3881-b0d6-2d337f656648 | -12.214 | -52.801 | 2026-06-17 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 587aa21c-5e3f-3ca2-a7b5-ff113aad259b | -12.1952 | -52.7821 | 2026-06-17 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 188.9 |
| be53670d-6123-348f-a2f3-d132d001606c | -12.2143 | -52.7801 | 2026-06-17 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 753078a0-6026-3722-87c8-672afaefbeb5 | -12.1949 | -52.803 | 2026-06-17 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 84c76929-0656-3440-a202-f0e2660bc91e | -10.1493 | -56.6115 | 2026-06-17 12:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 4c01b51f-5e7d-3e35-b3b9-4e673d619f9d | -8.9824 | -46.9766 | 2026-06-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 93cd78ae-3977-3d05-beb2-13a7cef1a731 | -12.2143 | -52.7801 | 2026-06-17 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 805d00bd-0ce4-37da-bf88-ffe22cc02f8e | -8.8222 | -44.8043 | 2026-06-17 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 07f819ab-dc97-332a-b261-e096d06fc35d | -8.8883 | -46.964 | 2026-06-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b3e7b830-91af-35de-8268-df7e847f71ed | -12.214 | -52.801 | 2026-06-17 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 549770cf-113a-3dc3-ae43-eeca7a05a1f9 | -12.1952 | -52.7821 | 2026-06-17 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 222.9 |
| 9526c994-b329-310d-8175-dc0c456f179d | -9.0013 | -46.9746 | 2026-06-17 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 6542dd6b-295e-3e49-9952-4fd2abdac6dc | -8.8222 | -44.8043 | 2026-06-17 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| d48f0ef4-8de0-3c74-9715-1fcff26f9d68 | -12.1952 | -52.7821 | 2026-06-17 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 239.5 |
| 2d25e762-74e2-37af-9e7d-9f9871663dc0 | -12.2143 | -52.7801 | 2026-06-17 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| fc2dcd2c-3c16-3ec6-af04-7797065a38d9 | -8.9824 | -46.9766 | 2026-06-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 7f22f1a8-9046-3b50-9950-dfa26e8a78e1 | -8.8883 | -46.964 | 2026-06-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a98fe9b0-b5b1-3b18-b15d-e8b1f1fa1617 | -12.1949 | -52.803 | 2026-06-17 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| e7c49800-43a9-3e9b-90cf-22eb1b342a34 | -8.9821 | -46.9988 | 2026-06-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 5233a827-67b9-3026-a6f6-992318a5a935 | -12.214 | -52.801 | 2026-06-17 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 32a6ac94-21aa-353c-91a3-dca4d85a5c5d | -9.0013 | -46.9746 | 2026-06-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 539c6a9c-07e9-3162-9905-d0e030f3ac98 | -10.1493 | -56.6115 | 2026-06-17 13:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 4a5c2ad8-cfbb-395a-9950-6d7912f26697 | -8.9635 | -46.9785 | 2026-06-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 98c273a7-150a-3110-ab44-7d5682636031 | -8.888 | -46.9863 | 2026-06-17 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| b6dc20f4-618c-3811-b4c3-26a9643f602f | -12.214 | -52.801 | 2026-06-17 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| ee35f66a-b9b5-3e45-b18d-7103a41c0ecb | -8.9821 | -46.9988 | 2026-06-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 5b183fc4-7cc1-360f-b1ea-425227d1122b | -12.2143 | -52.7801 | 2026-06-17 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 189.3 |
| 332c6bf0-76b3-3106-b61a-8ab9fe9e8e5e | -10.1493 | -56.6115 | 2026-06-17 13:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 9eae9b1a-3200-3169-a7f2-5d0013919f38 | -12.1952 | -52.7821 | 2026-06-17 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 236.5 |
| 3db977af-c5ed-331b-af72-c9e1e3a9d9b4 | -9.0013 | -46.9746 | 2026-06-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| bc5f7580-ea03-347a-89ec-fccd7e913e46 | -12.1949 | -52.803 | 2026-06-17 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0078700c-03f6-34f7-99f4-c91356becc29 | -8.9824 | -46.9766 | 2026-06-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 8e66025a-998e-3ef6-8555-3e62ad86c721 | -8.8222 | -44.8043 | 2026-06-17 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ee6dd80e-3867-35e9-8b90-a8539f7393e0 | -8.888 | -46.9863 | 2026-06-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e86cea2f-d8ea-363c-9336-be45f37d22d0 | -8.8883 | -46.964 | 2026-06-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 8ed2832b-f52d-3f8f-8fb1-17e92ef69df6 | -8.888 | -46.9863 | 2026-06-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c611c2fc-e788-38f1-a834-d83582d74404 | -8.8222 | -44.8043 | 2026-06-17 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 99f5b228-1a30-35a1-a63a-1c01805dd75d | -9.0013 | -46.9746 | 2026-06-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ca025044-fd45-303e-9a16-ad3630a1b935 | -12.8548 | -44.3625 | 2026-06-17 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| dbe4d3f7-fe39-3049-ae0b-655775bd1383 | -8.8883 | -46.964 | 2026-06-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 60ae922e-6110-31f8-9fee-5a5ff255afe2 | -12.2143 | -52.7801 | 2026-06-17 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 243.2 |
| a8ae1e44-c0f9-3d9a-a2a4-dd0d166a5ed1 | -12.1949 | -52.803 | 2026-06-17 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 419fdad2-1b16-3349-a67b-a397f44055fd | -8.9824 | -46.9766 | 2026-06-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f7108d83-b905-3814-842f-1009e594c15a | -13.2651 | -46.0559 | 2026-06-17 13:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b781854e-dc71-3b1e-87d3-f6f202b79b3f | -8.9821 | -46.9988 | 2026-06-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 4577483d-52b6-35a4-931c-e6beac3707c4 | -12.214 | -52.801 | 2026-06-17 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 947a0b3f-6d7d-34ed-bb92-d1acceb2c2ab | -10.1493 | -56.6115 | 2026-06-17 13:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 2ab91ec4-f00a-375c-9ade-bcf80b57849b | -8.9635 | -46.9785 | 2026-06-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6f7380d0-d4df-3602-88b2-c008d7c7895e | -12.1952 | -52.7821 | 2026-06-17 13:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 241.4 |
| 6440d10e-66b9-309d-9269-7b9c0dcd27d9 | -13.2651 | -46.0559 | 2026-06-17 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 9426d12a-68b1-3f9d-9d75-32ad1c69efcb | -13.2845 | -46.0528 | 2026-06-17 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| acf15f30-ed17-3fd7-95a6-9229f4f87766 | -12.8548 | -44.3625 | 2026-06-17 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d0324804-898b-39ec-a20b-7af9cfa0a1a7 | -12.1949 | -52.803 | 2026-06-17 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| edc689c3-c987-3ae6-b005-d36b605c5c06 | -12.2143 | -52.7801 | 2026-06-17 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 252.9 |
| 79abed2d-aa60-3377-bddd-30c35149796b | -8.8222 | -44.8043 | 2026-06-17 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a5226966-b875-38db-917e-d5b0fe5da11d | -10.1493 | -56.6115 | 2026-06-17 13:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 89268071-edfd-3ca2-a3e6-60e67b99c363 | -12.214 | -52.801 | 2026-06-17 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 94b21b17-f4c3-33d2-b345-125b37f539df | -12.1952 | -52.7821 | 2026-06-17 13:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 321.9 |
| 9b7c48b2-ea9a-3bee-94ca-472199334443 | -10.1493 | -56.6115 | 2026-06-17 13:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| ca1e78cc-ae31-3132-8414-6199b628e119 | -10.168 | -56.6101 | 2026-06-17 13:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 55942a78-015d-3114-ab49-04bd584aa0dc | -11.3603 | -51.4009 | 2026-06-17 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1e3eda74-6698-390a-bcfd-a089602b7239 | -8.8883 | -46.964 | 2026-06-17 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 67ce92ee-a6d2-3376-a907-ddd406242f41 | -13.2651 | -46.0559 | 2026-06-17 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d10d7bba-8e02-38ea-aec3-1a0b658bd2df | -12.8548 | -44.3625 | 2026-06-17 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| d791c437-79ab-334b-afa4-b0a69b0adc1c | -8.8222 | -44.8043 | 2026-06-17 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| abd76d36-4c8c-3bc0-b1a2-d0319fac181e | -13.9421 | -46.0367 | 2026-06-17 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6ca3a9ef-76db-3df7-b718-35d069618728 | -13.2845 | -46.0528 | 2026-06-17 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4639370c-2ae4-390e-9c0e-f67aced15bb2 | -9.0013 | -46.9746 | 2026-06-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 962dbfce-9605-3f5d-9325-787c579fb592 | -8.9632 | -47.0008 | 2026-06-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 2225fd08-e12c-315a-9c2a-0789c27c2916 | -8.9821 | -46.9988 | 2026-06-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| a037b21a-01cd-37ee-adb9-c1bf1d12a459 | -8.8222 | -44.8043 | 2026-06-17 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |


[Clique aqui para ver as próximas entradas](README19.md)
