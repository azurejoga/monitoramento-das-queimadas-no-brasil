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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f708190a-a85d-3ba5-b489-1aa281da4ef0 | -11.06069 | -45.96678 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6c57cf4a-dff1-3c41-8c79-a3330301c3cc | -11.0265 | -45.58403 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 40eb222a-0f3f-3fc2-97c3-6b29eda48259 | -10.98167 | -45.27279 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 84cad6ae-ed11-3e91-9d14-087d7297a07c | -10.85418 | -45.27887 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d5fe160e-9f94-3a13-9a3e-a289276117db | -12.67463 | -45.16162 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ae5dd399-c788-3c9f-b00a-54f85991ebd8 | -12.60608 | -45.35357 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 00da632d-dacd-3f07-9cbc-fa5e451a94fc | -12.70683 | -46.34178 | 2024-10-25 16:50:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0e00ff64-65e3-3d2c-81f1-ca81b2c04a0b | -12.50109 | -46.30463 | 2024-10-25 16:50:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 20bd8640-bfd2-35fc-9de1-01801191ef62 | -14.41006 | -46.4263 | 2024-10-25 16:50:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 01f3253d-848f-3c9f-b3de-6ba577b4762e | -15.84848 | -45.75019 | 2024-10-25 16:50:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7761ba98-e4e2-30c8-bbb6-f22eaab50a99 | -15.77308 | -45.69239 | 2024-10-25 16:50:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0f9667c3-025c-3787-94de-ecc73e83b62d | -9.22137 | -45.88027 | 2024-10-25 16:50:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c6b6898c-73f2-3020-b96f-b1842e53928d | -9.4294 | -45.9141 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 19de80ee-e18c-3f4f-be87-40e0ea731dc7 | -9.42883 | -45.91732 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3cddfa30-5570-3371-a168-8c04c7ef5b81 | -9.4281 | -45.91285 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b79eede6-2d05-3d58-80c2-7e097fb3155d | -9.4264 | -45.91913 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 026aca5c-8365-3fdd-9b13-c2d321d2d724 | -9.42565 | -45.91465 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| eb9958aa-007e-33af-adce-5c30ed4c0e98 | -9.42508 | -45.9179 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| e9782d9a-3ce5-33cc-8d7d-b72b542b8b52 | -9.42189 | -45.91521 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99f393cb-9159-3a07-9cd2-81ae85b09eae | -9.33233 | -45.96143 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fcb60f1a-fa17-3e1e-a610-f2a2a2b02c24 | -9.32859 | -45.96201 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 73670b50-dbf5-3bf9-955d-abad3c7cdcf2 | -9.22383 | -45.94115 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f1a8a4fe-29f9-3c0b-b076-4cc9b3af35aa | -9.21935 | -45.93736 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1f6c38cc-b420-38b5-912c-881260611ba0 | -9.21859 | -45.93282 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f984ff89-41fe-316b-9683-2bbbe222c628 | -9.41324 | -46.19624 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6ee19450-1165-3f4e-b990-764906fc6e95 | -9.40955 | -46.19682 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 222dcf1f-57ed-35a3-8b2b-a2db869c8837 | -9.40245 | -46.38179 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cd3dda13-4825-30c2-ab53-48f5fefb26ed | -9.36785 | -46.58428 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8089fdb4-d50d-311d-ba1f-ae4d52cbc24f | -9.36363 | -46.46693 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 49257d42-cce4-3588-a50a-6abc4f2a0266 | -9.33196 | -46.41039 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 997598f0-d4b4-3711-9359-b8af449d1bbf | -9.31294 | -46.43134 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a2011e7b-a63c-3918-a5e3-ad1acaff0971 | -9.30705 | -46.60542 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 501ee2c6-001b-3091-93b3-973bcf407e00 | -9.30344 | -46.60601 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 90886515-92a3-31b4-aed8-86dcf3dd7a9d | -9.29912 | -46.53288 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5294aa56-27de-3ce4-9054-4f817419a52c | -9.27328 | -46.21466 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f5ac5be6-1cbe-397b-9546-3e8d1df2745b | -9.2696 | -46.21533 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 41c34dc1-1cf1-3992-bce7-7f12d48054fe | -9.2659 | -46.21592 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0904d8b6-49df-3db3-ab3e-b18203d58402 | -9.26367 | -46.22525 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 685e742a-bd4f-3031-afde-9400d9e1caa6 | -9.92801 | -45.97185 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 2261c5b9-da1b-3aac-b7bf-f58e041a1030 | -9.63568 | -45.84589 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dcbd5ebc-188f-3fb5-ba74-df26928368db | -9.63149 | -45.84962 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 66627550-0c5c-3e36-892f-f7d744b06b68 | -9.627 | -45.84568 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e5b965a5-bccf-3abc-b6af-f895af31289f | -9.61572 | -45.82366 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cfc74dec-f0a6-3233-acfe-2a0828fc03ac | -10.79182 | -46.08877 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1813c8e9-caff-3d57-ae39-ab91a01ee26c | -9.91291 | -46.85714 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e3d4cb88-55e0-3de4-a12b-c323b3c2a0e6 | -9.90937 | -46.85775 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d687b4ab-f844-34ad-9715-180efd7ae695 | -9.88995 | -46.89404 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13824409-5d20-3f10-abf4-2619c28c0326 | -9.88642 | -46.89465 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79fb7b85-6a3f-30da-abd4-09b7d3de89d6 | -9.85771 | -46.27448 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9e971409-2719-3cfb-a550-9efc186050ff | -9.85477 | -46.27937 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9e444536-16f6-33f6-ba82-ec4112ef92a4 | -9.84307 | -46.07056 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8361431f-5311-3f7f-beba-d2383a68eff3 | -9.82932 | -46.26154 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 92c8ac7c-70a1-3260-8551-b5f637ff2c89 | -9.80633 | -46.28234 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d369106d-555a-3981-9e29-82a7177613ce | -9.80593 | -46.2788 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 109180c6-0108-3792-8c3f-bbac13e6c568 | -9.80563 | -46.278 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d95ff2ba-6ed0-3713-9412-caf00573b987 | -9.8052 | -46.27444 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 83f49656-bec2-3a00-9c1b-4ba26a96b3a2 | -9.80493 | -46.27364 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9bba9003-1ef1-3037-8ab4-afc5a1bf5cf6 | -9.69143 | -46.76812 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1ca5d07d-b8f1-3318-abd7-3ea715445fe0 | -9.69121 | -46.24255 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8451ba06-2791-36e9-9d87-42f9e6875207 | -9.68785 | -46.76868 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 20461ae3-12c7-37f8-9189-9935489870b8 | -9.68755 | -46.24315 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 710ab367-3c43-3811-81c0-0140bb808728 | -9.68495 | -46.7733 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 93ce5d00-4d3a-33bf-b754-d36bf93fa91b | -9.68427 | -46.76919 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8c2c5552-35b0-3a27-b2e9-47399ba056ff | -9.62532 | -46.231 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 603c2b72-fc2f-3645-b01f-41525aaf8024 | -9.62166 | -46.23164 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 32aca238-0449-3644-849f-7e31cc103d9c | -9.6038 | -46.76381 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f6c861e2-f4cd-3d29-8731-6d86f74d9096 | -9.60313 | -46.75969 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 1d03e388-a892-32db-b1cc-2f4a1e188fc5 | -9.58965 | -46.42653 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b4aeac5f-9fb0-3c70-99da-72acabedfa91 | -9.58651 | -47.12741 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| faa4940d-8edb-3efa-ba6e-ee021e2c7081 | -9.55322 | -46.31758 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 490582a8-95f8-30c9-92b9-923235fd7c02 | -9.54077 | -46.70609 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e4334d9-8ac7-35a7-8731-20dac84faa93 | -9.52486 | -46.7215 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5efd33ed-0208-302a-a5c2-92ef83976495 | -9.5232 | -46.08769 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 298a38d3-f683-387b-b5d5-580fc34fb95d | -9.51961 | -46.80251 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 329b762c-de92-375e-840d-6b72586a3082 | -9.50483 | -47.23 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1ab100a7-be64-3acd-919b-216498a604e5 | -9.50086 | -46.61866 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b902e3b0-bb33-3451-85b6-acab7ca0abc2 | -9.50069 | -47.22662 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 79a966b9-4e81-3753-84da-14bfb7ae7928 | -9.49782 | -47.23116 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2df8cca4-e897-31cf-9ee9-46ec4213d78b | -9.49725 | -46.61919 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| cc0b23f2-6fc6-3903-a56b-a59cf8e90e87 | -9.49719 | -47.2272 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 59894408-17db-3119-96f9-99717e50a215 | -9.49656 | -47.22322 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 8749b44e-cdae-3d1c-908a-4c689260e186 | -9.49369 | -47.22777 | 2024-10-25 16:50:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 21b1645a-d90c-3310-8644-1e9585e2769d | -9.47043 | -46.72609 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43c87fd0-46b3-3114-b636-65b9f2753131 | -9.46752 | -46.73078 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 854f9260-7603-3161-9145-d7323816d72b | -9.46684 | -46.72668 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c0be5517-18b4-3d24-a826-3c6248334e0a | -9.46617 | -46.72259 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2d70d48a-819d-333d-9e53-05d2ce466dc7 | -9.46259 | -46.72318 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61018439-79b5-3fd9-b73f-81862fb69438 | -9.46213 | -46.69799 | 2024-10-25 16:50:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 08db62c7-9e6a-3ae4-927d-96343450bcb4 | -10.05373 | -46.0971 | 2024-10-25 16:50:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a356a47d-f6e9-3819-9b58-69f8c890a8a7 | -10.43376 | -47.33566 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2f25e903-8252-34ee-882f-9793442d2d95 | -10.43313 | -47.33182 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 19f7f2ee-38a7-358a-8d9b-29c46054a6f8 | -10.42968 | -47.33238 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4ed89d35-a663-32e9-bba3-e41cdcc702a2 | -10.42905 | -47.32853 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2d9c8d25-a6b7-339e-b83f-840d98a1dfae | -10.39221 | -46.58828 | 2024-10-25 16:50:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0c3c3e63-5da3-34e4-b17d-8d53b789c35b | -10.39154 | -46.58413 | 2024-10-25 16:50:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f930cbbb-ebdd-3516-881f-0620432e1e50 | -10.32617 | -47.43137 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| aef9ba3a-2446-3e21-8789-e8c2ecca3605 | -10.32476 | -47.43948 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 05332f23-d517-3de8-90f1-e4644ba8fd0e | -10.32396 | -47.43956 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 01f718b6-3cc6-356c-9bd2-9958d81d0386 | -10.32355 | -47.43183 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d1bf5b46-b117-331b-a4de-49f4895d52b9 | -10.32272 | -47.43193 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README147.md)
