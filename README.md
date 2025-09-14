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
| a6fbe1fb-876f-3108-aeeb-9436501620e6 | -3.5908 | -58.5963 | 2025-09-14 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 64a88149-c510-3003-92d6-b1bf413d1ac2 | -3.5809 | -47.5367 | 2025-09-14 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 134ca8c7-3e9d-37de-8a1d-8bb274864dae | -3.5994 | -47.5359 | 2025-09-14 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 5e0aae43-233b-3216-b3b7-fe90ad1d9198 | -12.7863 | -48.0209 | 2025-09-14 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| cc828945-3722-37a3-9285-8f39c2b448b1 | -11.2349 | -44.7751 | 2025-09-14 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e2fc6469-da2c-3642-80a5-315e09cd68f4 | -3.581 | -47.5149 | 2025-09-14 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 207.4 |
| 6657cdb6-5bc0-327a-a3a5-2b68338851ff | -8.9548 | -46.1975 | 2025-09-14 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e3e658e0-7d4b-3772-b5fc-b98f9542e016 | -12.1424 | -47.5987 | 2025-09-14 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 5a61b1ff-c7bd-39be-a683-2b37f69ad893 | -10.1612 | -64.7213 | 2025-09-14 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f1e3b145-74c2-35f8-b697-56b381942d7b | -10.9163 | -45.5775 | 2025-09-14 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f38abb9d-427c-32a0-968b-1af29814f7f8 | -11.7011 | -59.3061 | 2025-09-14 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| e366df09-c464-3a6c-9a68-198031f11a8f | -8.9362 | -46.177 | 2025-09-14 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 14f0a319-b183-3fb2-a764-712c5eb78ce6 | -8.6795 | -47.096 | 2025-09-14 00:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 54059084-2d53-361e-90f0-7d78e9c91dc6 | -23.175 | -47.5708 | 2025-09-14 00:00:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.0 |
| 52b0b910-1b13-348a-9d5f-6a377c29ebd3 | -3.6181 | -47.5134 | 2025-09-14 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ed2232c0-3207-35f7-9a45-687074ff8c00 | -15.1883 | -48.7225 | 2025-09-14 00:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1de589ae-2242-3960-ab2a-1cefb5c23ab6 | -14.6212 | -52.048 | 2025-09-14 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 5b8758b3-b7f5-3e1e-b6ee-92fc81910148 | -11.464 | -50.7741 | 2025-09-14 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bd5c7d3e-2bfc-365c-a1cd-f98ce9e1de41 | -11.7009 | -59.3257 | 2025-09-14 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 78649d78-2240-36dd-8197-5de921c139bf | -12.1427 | -47.5763 | 2025-09-14 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 64d04b88-1544-3847-82ae-b0fd99539189 | -14.6215 | -52.0266 | 2025-09-14 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 424.1 |
| c65d0df3-705e-3d17-a1b3-22dca5206a68 | -14.6409 | -52.024 | 2025-09-14 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 359.8 |
| 597f8315-4963-3fd0-b4db-897b208a9a60 | -3.212 | -47.1357 | 2025-09-14 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6a7b36eb-fed1-3d62-9537-085d93f251dc | -8.974 | -46.173 | 2025-09-14 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5f977631-fd49-32c1-8ca4-952fb441c3b5 | -12.1615 | -47.5961 | 2025-09-14 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3a380554-438e-3f6b-8d88-d071a348bafd | -11.445 | -50.7762 | 2025-09-14 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 46cf4276-e331-3f9a-bd00-29caeb4dd05f | -14.7529 | -60.2123 | 2025-09-14 00:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 249eec7c-ddb5-3aa5-84f2-e86c2a5b6790 | -8.9554 | -46.1525 | 2025-09-14 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| fc6d3c6e-54ff-3041-9d9f-1b445c8871e6 | -10.7816 | -48.1256 | 2025-09-14 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 7dd7fd2b-bc2d-3c58-a10a-b90b528d8e37 | -18.7282 | -51.7816 | 2025-09-14 00:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 728babcb-2e51-3eae-b777-d171b80125df | -23.1538 | -47.5765 | 2025-09-14 00:00:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.2 |
| bd4f67b0-e57d-3f34-a4ad-85e6ecc025eb | -14.4779 | -47.3368 | 2025-09-14 00:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2212af66-8cdc-3278-9bc8-9d84f83ae9b7 | -12.7867 | -47.9986 | 2025-09-14 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 89876ab3-e3a1-31ec-97c1-6ce7c183031d | -7.6131 | -46.7078 | 2025-09-14 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 95680556-dcd0-332e-8d62-e59f1532ff89 | -11.426 | -50.7783 | 2025-09-14 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ae8415ef-a19c-37f4-97ba-0ef99be2a69e | -12.4541 | -57.7872 | 2025-09-14 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4c77e847-ff3c-3637-9ab5-2d47e80aab68 | -8.9737 | -46.1955 | 2025-09-14 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| e627ddb8-41b5-386b-95ec-95460f174171 | -8.6793 | -47.1182 | 2025-09-14 00:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| cabc9e1a-a91e-32e0-9bfe-d19d7fe88403 | -8.9551 | -46.175 | 2025-09-14 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 80b9690e-22a8-3dac-be95-c98a1e7a2142 | -21.6436 | -50.2026 | 2025-09-14 00:00:00 | GOES-19 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| 7f5bd4d4-ca24-3019-98e8-0b48dd7dabb2 | -12.9294 | -54.7333 | 2025-09-14 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0a21b22a-5774-3a85-87b7-a9e895821839 | -18.7082 | -51.7851 | 2025-09-14 00:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 3d329e76-838e-36e9-acbd-1b2a67ba6915 | -14.6405 | -52.0454 | 2025-09-14 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 3eff89ce-a5f1-3c56-8ace-1c20bc47f16b | -3.5996 | -47.4923 | 2025-09-14 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c1a26ee0-922a-3895-88ae-8c3919b0e830 | -11.4447 | -50.7976 | 2025-09-14 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 26f35a8e-6873-37ee-8c4e-b492a78ee171 | -3.5995 | -47.5142 | 2025-09-14 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 319.4 |
| ed199982-626b-3d6c-9afc-73173018a387 | -8.9362 | -46.177 | 2025-09-14 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 3d70f69a-b5e0-355e-8634-87c09b262f6b | -8.974 | -46.173 | 2025-09-14 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| cb4a6ae9-3c32-35a0-b1d0-f59f0bda9e18 | -10.9163 | -45.5775 | 2025-09-14 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| fe709aed-806e-3f82-9bad-5a472538accf | -11.7009 | -59.3257 | 2025-09-14 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 00022206-05f6-331f-b087-3833c963627f | -14.6405 | -52.0454 | 2025-09-14 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 3969e160-3663-3b2f-8a61-827317dc5fab | -8.9551 | -46.175 | 2025-09-14 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 39c9ff4f-a97f-37b6-9ea4-8627e4643c4f | -18.7282 | -51.7816 | 2025-09-14 00:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 33e7db13-acf8-3a29-9b7e-f0ddc620524f | -3.5809 | -47.5367 | 2025-09-14 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 408b9f38-d89c-35ab-9f1b-fd237738bf4c | -11.464 | -50.7741 | 2025-09-14 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 211.7 |
| f579fe31-d2f2-3faf-8d7d-d33c3ae71629 | -3.5994 | -47.5359 | 2025-09-14 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 11556105-ba81-3d16-a84d-7bdf1727e313 | -10.7579 | -44.7721 | 2025-09-14 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8fe57d93-d8e8-3c18-a183-6d878bc4ae49 | -12.9292 | -54.7538 | 2025-09-14 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 8e87cf85-fb01-31c5-b32f-e172b6369815 | -11.4447 | -50.7976 | 2025-09-14 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| d2242b75-d78f-3135-a520-0d5b05742eb1 | -14.6409 | -52.024 | 2025-09-14 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 238.7 |
| 3337a5e4-bc50-37db-a657-fb345ab520f0 | -23.1538 | -47.5765 | 2025-09-14 00:10:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 23eeba73-1f9c-3062-8579-60845a1fef86 | -11.426 | -50.7783 | 2025-09-14 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 03d70eba-36f1-37f1-8601-a786e10fda91 | -12.4541 | -57.7872 | 2025-09-14 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e74e3013-4310-3a76-bfc9-c9d65f5c4aaa | -3.5995 | -47.5142 | 2025-09-14 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 312.2 |
| 29940026-fbae-35bf-82dd-ab0836fbffb6 | -8.9548 | -46.1975 | 2025-09-14 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ec19b92e-5031-3c18-92a9-cd95ae8bfdcb | -14.6215 | -52.0266 | 2025-09-14 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 55be3080-733a-3148-8902-8e595489a73b | -11.4453 | -50.7549 | 2025-09-14 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 1fa72ae0-766c-3c70-a872-f342ef2414e8 | -11.4637 | -50.7955 | 2025-09-14 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 35286f50-79dc-3c26-aa69-f9e7c9f11df7 | -11.7011 | -59.3061 | 2025-09-14 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 9f4f4874-f3dc-3cc1-9043-cd06521426de | -3.6181 | -47.5134 | 2025-09-14 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 25239a12-0693-35ab-b781-1c8a6b78029a | -10.9167 | -45.5546 | 2025-09-14 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 12e9631e-cee8-38f1-9fd4-b2921b7b4b15 | -11.5348 | -53.9469 | 2025-09-14 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ebd6e087-4ca0-3202-86cf-05069f6a27f4 | -12.7675 | -48.0013 | 2025-09-14 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 23e2b944-ca82-3f00-be3f-1a47bd6e11ed | -18.7082 | -51.7851 | 2025-09-14 00:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 6ba3865d-9666-3380-ac3c-b3d0ddc52787 | -12.7867 | -47.9986 | 2025-09-14 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 17556e26-4694-3634-a593-1c5d73244f0e | -8.9737 | -46.1955 | 2025-09-14 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| be3c3a42-bf5d-3fc4-b1cd-9acf9a5fc103 | -12.9294 | -54.7333 | 2025-09-14 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 6a5ccd07-49dd-3a48-9c50-0061fedbacce | -3.5908 | -58.5963 | 2025-09-14 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a8fd500d-0d2c-3e6b-8c36-47c356bf6dd7 | -8.9554 | -46.1525 | 2025-09-14 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| d9065de1-ff5e-3561-b193-ed08de7fa179 | -3.581 | -47.5149 | 2025-09-14 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 160.7 |
| a7dfb4da-bd06-392c-a952-355fb702039c | -12.7671 | -48.0236 | 2025-09-14 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 51ecf56a-dda8-3e1f-97f7-a54e418cda5a | -11.445 | -50.7762 | 2025-09-14 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 284.2 |
| b083448d-9bbd-3f9d-9164-4c54bbdb9547 | -12.7863 | -48.0209 | 2025-09-14 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 5b1a393c-d884-31e2-b200-7f72a65813b2 | -7.6131 | -46.7078 | 2025-09-14 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 75366da2-bb94-3108-a499-45d49584b2a2 | -11.4447 | -50.7976 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 07850cee-805d-38e5-b749-9e7319178528 | -11.3301 | -50.8528 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 88bae128-1aa7-36b1-b53b-29f906b6a784 | -21.6668 | -50.1064 | 2025-09-14 00:20:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| 837fe913-d48e-3939-9136-fde3a26c2f59 | -18.7082 | -51.7851 | 2025-09-14 00:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ee4b256d-dda1-3923-90d4-568d4e8ef58f | -3.5908 | -58.5963 | 2025-09-14 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 136507da-beb0-3265-afe4-766ce2f5609c | -8.9548 | -46.1975 | 2025-09-14 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6c50f120-5106-3ef0-ad2e-4a38222613c9 | -10.9163 | -45.5775 | 2025-09-14 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 118d81df-a797-3e4f-8f49-222eb5335d3e | -11.3304 | -50.8314 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 168.8 |
| b808e187-c6a1-37f4-9630-6058fc033d61 | -3.5994 | -47.5359 | 2025-09-14 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c0c7a044-3beb-3495-b98c-b7c5dc323be0 | -11.464 | -50.7741 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 8f471ca4-444d-359e-bf41-4353bf18e275 | -3.581 | -47.5149 | 2025-09-14 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 763fccdc-7cd9-3cb1-9ec8-d46127549b99 | -11.445 | -50.7762 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 9c0663a3-b94d-3c71-965c-4a33941cb89b | -11.3494 | -50.8294 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 125d5a8a-d1ab-3aed-8c33-439cba7a484e | -3.5809 | -47.5367 | 2025-09-14 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 96514f0f-4f2c-3af4-a3f2-1a0a6bc12b77 | -3.6181 | -47.5134 | 2025-09-14 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 966b8eb2-50a0-3b82-ab9e-3d5ba2eaa204 | -11.4637 | -50.7955 | 2025-09-14 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |


[Clique aqui para ver as próximas entradas](README2.md)
