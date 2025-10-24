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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3348ee42-32a4-32c3-abb0-4809227c658b | -12.81351 | -50.94388 | 2025-10-24 03:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58d00688-1dc6-327b-ba44-af9e160b49a8 | -3.86987 | -48.33612 | 2025-10-24 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3b58bdc6-130d-30e9-8700-5f7e2725beff | -12.2978 | -45.5335 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aeda5b6c-778b-3316-8d22-591142db6287 | -3.92253 | -47.69476 | 2025-10-24 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0407a568-96ef-3d5a-9dc9-f0c287ee26b2 | -2.42214 | -48.4439 | 2025-10-24 03:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 721df8e0-b0e7-3bd9-a0aa-b0379faed49e | -12.29313 | -45.53252 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 03ba016a-c386-37f6-965c-4b0e0af5459c | -14.46293 | -47.9147 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31038365-2905-34ab-b9a7-cce5903bdbc4 | -3.8157 | -42.46826 | 2025-10-24 03:49:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8508d1-3c91-3d89-99fb-9ae3fbcb3fdd | -15.83354 | -49.10363 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f67cd37e-2eae-36b7-a89e-9818d8b806c3 | -12.01625 | -43.88559 | 2025-10-24 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 411b2f1a-48bf-365f-994e-462816ab3c72 | -10.8748 | -45.08408 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e07e173-8238-343f-90f4-55b605c1edbb | -11.34331 | -45.89658 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cef4df38-4f99-3a02-b84b-d07fb9d8e38d | -11.05875 | -45.39841 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 002f55db-86f2-303e-bd5b-d53fd77e7aea | -14.44035 | -50.94287 | 2025-10-24 03:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce61e261-e3b7-3de6-96ac-195e90fdbef3 | -5.5838 | -41.31828 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 78736e17-3fe7-33db-b066-91813f8edee5 | -14.03598 | -48.72935 | 2025-10-24 03:49:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ef3394b-378d-3dc1-a752-e73d273f49c5 | -10.88761 | -46.04451 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5f77f17-d0f2-32d6-973b-35b655c9bf13 | -14.74639 | -46.60997 | 2025-10-24 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7b07800-13a6-391b-aea5-cd99cf1d6c99 | -2.82097 | -49.14475 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0547da8d-d941-38d8-8707-12f871be7bf1 | -14.7512 | -46.61095 | 2025-10-24 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 219dccf3-a50a-3c84-aa3b-4cd820fe0d76 | -9.44813 | -46.09697 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28ec497e-d240-3e47-acf0-87eeafad1771 | -15.44946 | -48.57894 | 2025-10-24 03:49:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcd46da9-ea15-3951-889b-51242689107f | -3.24126 | -48.76629 | 2025-10-24 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16858568-cbe1-3e10-b553-0a923f0ffacb | -12.86956 | -48.59891 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c111e2f-59b8-364e-bd23-4dffaaac6542 | -9.64009 | -46.90045 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1acb6526-0c2b-3196-a83c-5a0d4f02b6e8 | -10.56036 | -50.00364 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 481ba81e-9725-38d6-9b53-c385d0b25a8d | -2.47331 | -49.22998 | 2025-10-24 03:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9c2dfe37-547b-3a3e-a402-c5f2bb349167 | -5.52218 | -43.87245 | 2025-10-24 03:49:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 711c40cb-d4f1-3432-9112-775f1c9305d2 | -10.01609 | -47.1046 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5636b383-60c9-3a4b-8363-9a8e8f1bccbb | -15.31812 | -47.85194 | 2025-10-24 03:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 640acaed-29ca-3816-8815-fd57aec5df84 | -9.86894 | -47.46853 | 2025-10-24 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ca6af59-5ba6-3825-b1f3-889220722ef3 | -9.44868 | -46.09391 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b3c4d7b-5e88-3d30-865c-10783f2cf8ca | -11.00906 | -47.90556 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 088e560e-39d0-3c09-ba28-555d64338bbf | -11.05591 | -45.38711 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68cd8e13-d93e-33b9-b557-fd8920a3e3eb | -15.83444 | -49.09938 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ca1776db-a827-3f20-865e-856561bbde3c | -3.70535 | -40.42382 | 2025-10-24 03:49:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e2525765-9847-3bc1-a476-aca1c681b4c5 | -9.23462 | -45.6219 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27474b7e-adbe-3569-b054-25fd893d2a9a | -9.23481 | -45.61884 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50561fdf-6103-37c3-ad92-9e1f97179c82 | -13.77055 | -48.34224 | 2025-10-24 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b704f590-2e7b-3eb3-b48c-2f522aa78764 | -14.77042 | -44.97016 | 2025-10-24 03:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 412b7673-41fb-3509-be8d-25e88feafd66 | -11.147 | -44.94147 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69074b8e-dc64-3a38-b4bb-69fb24eaac5f | -12.24638 | -47.03095 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3856469a-abc3-3e8b-b0f5-79ee0aa0722e | -4.91377 | -47.33049 | 2025-10-24 03:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a63bb8e7-2fa0-3238-bba0-286091d06320 | -3.92459 | -47.6928 | 2025-10-24 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc190be9-a20e-3fc5-b198-764bef1d9c23 | -16.64507 | -43.70992 | 2025-10-24 03:49:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23471f66-53fe-3348-8c01-b1b22eb851d7 | -13.15652 | -47.09397 | 2025-10-24 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f20b454f-7db8-3277-a417-fb8d9edd9d65 | -10.62475 | -48.08268 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c813f0ba-93af-32fc-b172-7dc425bc0d02 | -11.57608 | -48.57244 | 2025-10-24 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d606792-5b85-3048-b45a-7fbc7998f8e2 | -12.71891 | -46.94453 | 2025-10-24 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39e65c03-1023-376d-ad3b-0eb69bad5fcf | -12.06679 | -46.40434 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb87e8b4-885b-33bc-926d-accdd3f66eac | -10.04138 | -47.09854 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdd5b1a3-fe2f-3ae9-873e-e6c5f85feb7b | -17.04196 | -42.7298 | 2025-10-24 03:49:00 | NOAA-21 | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 441f6b58-0096-344d-b0a3-0cc525a55663 | -12.80988 | -48.63189 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88284f52-b24c-3571-b65e-6e6976877c25 | -11.36449 | -45.93142 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a5f03a7-8ceb-386d-bab1-c9418cce537a | -13.2162 | -47.73772 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37a17d67-b0e9-3a10-a943-db95140d9989 | -9.31143 | -45.20486 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56d619f8-d66b-3b4b-b801-33e71765d86b | -16.47898 | -46.47766 | 2025-10-24 03:49:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f09b63b4-d287-3f1d-b88d-6fdf4dac9620 | -12.2761 | -43.82327 | 2025-10-24 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6200ac0b-b027-3834-984f-add5c7421237 | -3.69943 | -49.5699 | 2025-10-24 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18a4cd97-f693-339a-9689-6e2e07eac105 | -16.25326 | -46.78172 | 2025-10-24 03:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b1a879f-fae9-3744-9fb4-0ddae46256e1 | -10.01937 | -47.08692 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f69ed8b-a794-3404-9305-399ed433c401 | -4.30995 | -48.22746 | 2025-10-24 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d4722f9-a1cf-3508-adee-eed6f98c01e7 | -13.28697 | -47.48809 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68a19abb-a479-3c06-9d12-218dd5a99d63 | -11.06669 | -44.78511 | 2025-10-24 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc73c2b5-55d1-3da8-ad0e-cd8bc3b006d9 | -11.98989 | -43.32059 | 2025-10-24 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56cdebed-7799-3777-89df-183de546cf4e | -4.906 | -43.21618 | 2025-10-24 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35e2d376-9c87-3f03-83d6-be0a672a61ec | -5.53731 | -41.35279 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61714955-a268-3722-a077-b6a9644cb2b8 | -9.93217 | -47.46278 | 2025-10-24 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84483b5f-ce56-3d68-bc38-9e853cb31f72 | -14.77827 | -44.97614 | 2025-10-24 03:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b169c1b4-3cbc-3e24-81df-022a0cd69890 | -14.91914 | -48.13868 | 2025-10-24 03:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09c5f95e-f2c4-39f8-a2cd-fb2804841fd6 | -11.35363 | -45.9513 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8cd36d8a-1893-3d2b-a256-f94fe852c63b | -10.95031 | -50.37529 | 2025-10-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4fd10e14-80a1-306e-ba12-399da4d53416 | -10.96236 | -45.07944 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c20319e-c439-338a-bffd-0099064ac8c9 | -13.88454 | -48.37285 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7580e499-400c-32bb-b1bd-f252dcb17b74 | -3.24228 | -48.7604 | 2025-10-24 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dff4a069-f2d1-3547-a813-80ae91521a17 | -9.31043 | -45.21034 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37367b48-6b26-34b8-aa79-a7b8eb4cb9de | -12.07176 | -46.40541 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c748c777-36d5-3f35-b963-2d8a012ec8fc | -13.24534 | -47.88589 | 2025-10-24 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5ffa820-34d5-3b50-83d2-1f3031590341 | -13.80715 | -43.89268 | 2025-10-24 03:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 092c7e21-d07e-31dd-b7f9-d35509764b78 | -10.56891 | -49.99405 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8dea8987-7671-339f-8822-4e6dbb1796c2 | -4.89908 | -43.22935 | 2025-10-24 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a7f3056-3e93-37dd-abfe-f56b2560d2a6 | -9.2698 | -46.45433 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 155baf49-59c5-30d7-8c93-91da36fb7c0a | -11.03217 | -47.90628 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 07ce201a-f084-3b45-a769-76a6e24dd878 | -3.02489 | -49.44471 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 163dcaad-7bec-346f-93d9-fd5f2b6b8daf | -13.3524 | -47.97696 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8eb020b-881b-3d7f-a134-a67046217b5f | -13.3358 | -47.96666 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68311fce-77df-3962-9a60-b558faeccf37 | -13.90967 | -48.39009 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffb901d2-46d3-3cd8-b14c-d71e13753998 | -11.36726 | -45.94361 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 527649fb-10bf-3b7d-8c62-2b1790dbafbc | -5.61791 | -41.11084 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ce4a1fc2-09dd-38e1-abaa-149efa6f1f53 | -3.29707 | -43.49545 | 2025-10-24 03:49:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a8c8dae-5539-3dba-bd9d-94247fc8caa4 | -9.60272 | -46.90934 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4cb59f13-6544-340e-ad0b-47f9bcf5ed85 | -10.47104 | -49.09619 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 932b1927-259c-3a12-9fa6-217f92c58a7b | -6.52013 | -37.47996 | 2025-10-24 03:49:00 | NOAA-21 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 49c8538f-5465-315c-b789-caa3e8838534 | -12.31387 | -47.27126 | 2025-10-24 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5966e2a8-00fc-3426-b13c-95eff79b4942 | -3.301 | -43.50142 | 2025-10-24 03:49:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a13ac731-d3a5-300f-9346-1826b5d9c54d | -10.03994 | -47.07682 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5ec46d9-9209-3bd3-bc4d-13977e8b426c | -16.54758 | -46.43736 | 2025-10-24 03:49:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 050fc380-762f-3a12-b17a-819ea50cfb9e | -13.35977 | -47.96816 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44c1d1f7-212d-3e6e-80ea-758e33e50c69 | -6.08702 | -40.56971 | 2025-10-24 03:49:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a43ef16-6fd7-3eb7-b8a8-17ba036e002d | -12.29516 | -45.53147 | 2025-10-24 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |


[Clique aqui para ver as próximas entradas](README10.md)
