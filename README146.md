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
| 2ac07172-49c2-3ccc-b059-2599164a56c5 | -10.90767 | -43.86863 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e4a483b2-e65e-301a-937e-221da255050d | -7.36442 | -45.41282 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b6f7e34-f0c2-3d58-ba7a-7f4a917af6b8 | -8.97697 | -44.15489 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| dd05a33a-67c7-3077-bf7b-31d9889cf60b | -10.6907 | -56.66908 | 2026-09-28 17:09:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| cd557379-e1aa-3346-ab04-d34154ca7b6f | -10.99846 | -50.69621 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| fb51ec94-043e-3c26-a3f4-eab8f143294b | -10.91338 | -43.86726 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 673ab47c-fbee-391a-9fd6-ad4b213a10d2 | -11.84533 | -47.78645 | 2026-09-28 17:09:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b73b24f3-d1f7-36ab-955d-32487a7005ac | -10.19827 | -49.99263 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b1914668-bfcf-3419-b764-02edb30f4f1c | -6.23655 | -53.03214 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| dce9c281-53d5-3912-ae49-2a1d6aa37a62 | -10.89233 | -53.9342 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0ce88d2-a93b-3599-9db3-ec20d66bf989 | -10.95814 | -43.88274 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 45334ef4-dd26-3eb3-b82a-6410c95f1854 | -10.81709 | -57.19319 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2105b322-56af-37cc-9ba3-0efd7ccab94d | -9.50898 | -46.36654 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f470fa80-2ecd-32ea-bd65-8fe5f61eda25 | -9.76198 | -44.84631 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1d760543-0f0d-3aea-bf47-fa5c255e82f0 | -12.81302 | -54.00403 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9c270096-9c5f-387d-a8bb-91dd103d555b | -6.70119 | -45.67672 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| c82b789c-8755-316f-8f3e-64bd7a0dc621 | -11.85509 | -50.88589 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a50d4c04-0956-3a47-841b-a6be5aaa4a86 | -7.06011 | -55.48247 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ce1c71dd-542b-314e-8eac-48a4194b919a | -9.84624 | -48.39901 | 2026-09-28 17:09:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a182932e-cea3-3683-8cc3-a081cf5df78b | -8.39231 | -44.75541 | 2026-09-28 17:09:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6d81e1d-a672-3796-b4a2-45a2330253aa | -11.90312 | -49.98695 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6264c2de-b7d5-3922-8d34-88242d6b98c3 | -12.79926 | -54.00261 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 96b09db5-df4a-3d41-9d97-503f467054c9 | -8.67099 | -45.38263 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 923de97b-8369-3a78-bb3a-f97d120cdb8b | -8.97389 | -50.97861 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c5d6bd2d-67b9-3037-8315-e5613c22d99d | -7.25367 | -43.35432 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cce93ac5-1f98-3721-ac5d-77936b1d8d28 | -11.08353 | -46.08227 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 221f9863-1dd5-3344-9755-dab7a1896f7b | -10.95991 | -50.69358 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b19fae67-1912-31f9-a0e2-69d02f9457bb | -7.05656 | -42.86749 | 2026-09-28 17:09:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 8e6cde0f-3f50-3008-9f2f-9c857362076b | -8.23709 | -45.40222 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 44648b16-a4c5-3aa0-a718-bf0e50c554e6 | -11.56662 | -47.39502 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 73380ee8-8f36-36ff-a8ee-27966e24de84 | -6.88524 | -55.55957 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| eea5b2c8-2ffe-3bd3-893a-7bd92a4a2bff | -12.28516 | -50.26723 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6ea023d4-4a87-35cf-88d8-5f76e677e59e | -8.93581 | -47.42391 | 2026-09-28 17:09:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 82a4b42c-b372-3eb2-983d-8d31ac40f889 | -11.84455 | -47.78211 | 2026-09-28 17:09:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| ce245ba3-e728-3e22-aab3-5161c6933ca5 | -6.13845 | -53.05502 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 52b3f98b-63d8-35b9-8ea7-2d5e3e9b0022 | -11.52257 | -47.38405 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c183efb5-fad7-31ac-951c-ff68d7b3f7c8 | -10.21415 | -50.01564 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8cba7cff-08f3-3c4d-9700-4f7845b3f4a3 | -9.11612 | -49.90176 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 135a6f64-96fd-3571-804f-25117f4092a8 | -5.24773 | -44.92923 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 94aa7d8a-7b76-3557-ac3c-132950c32303 | -11.0118 | -54.13812 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 54dfc861-ac27-3002-842a-7a0da812f456 | -9.07219 | -61.43732 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b2c706e8-af58-3cc8-8b67-ad3206cee1c9 | -8.64432 | -45.75727 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 500f2c13-a8e9-3ef2-8f65-84d957c7159a | -9.87012 | -43.62494 | 2026-09-28 17:09:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 64c015b9-ddb6-3fe6-82fa-b68c71371b28 | -6.46775 | -55.00991 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b6deda22-512d-3540-9c01-b287b83dfc29 | -12.10992 | -57.18248 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5f08146d-d8c7-310c-a64e-bcd8bf434f14 | -8.28489 | -54.73057 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0474270d-6158-3452-b195-737f9cf65869 | -9.73182 | -53.94994 | 2026-09-28 17:09:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 83807187-3c19-3f2f-bf27-a8f8525219c4 | -6.19998 | -52.9136 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2eb62c02-499f-3730-8398-d6f3f6d9acc5 | -11.57993 | -45.46655 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e063ed1b-596e-3da0-946a-e4badc69c964 | -12.15071 | -50.37669 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b74b5d57-0dd8-353b-b1fe-2c1780b93934 | -11.36717 | -47.44343 | 2026-09-28 17:09:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f87177c5-745f-3a63-8b26-a2f4590a24bf | -6.71967 | -55.07592 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8c14db71-c7ce-355f-9423-bd8b68c7928b | -6.21052 | -52.91202 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| a394866f-4882-3319-ac5c-fc5e12a60986 | -10.04678 | -63.96197 | 2026-09-28 17:09:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 848ccbca-32a0-3ceb-9a42-2af9bc28e728 | -9.35433 | -46.53862 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 2d67cb03-4a1e-3bc4-9cd0-0056454f4ca7 | -7.03873 | -45.81682 | 2026-09-28 17:09:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67d00e6b-5721-39ec-bdad-efb58fb25101 | -7.3938 | -42.63683 | 2026-09-28 17:09:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f9592567-dfeb-32bb-a948-fa92c4f65032 | -8.66911 | -45.37206 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e0eee9a7-3db0-3081-9db9-756daa719674 | -11.73861 | -54.51247 | 2026-09-28 17:09:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6a8987ae-1a9c-3b48-a854-a147fa1abb0e | -10.57626 | -46.36119 | 2026-09-28 17:09:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cda3093e-1873-392f-9973-022b02b5fc83 | -10.07035 | -59.41379 | 2026-09-28 17:09:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c50c139f-5186-3e88-85ef-cf5c1b84f4e7 | -12.3927 | -50.23683 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6ede2cae-d97a-3387-a96b-9a794fcef12b | -9.39927 | -46.38758 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3806b741-518c-30df-a83f-736b34a567cc | -6.31364 | -43.61819 | 2026-09-28 17:09:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 18cc9483-5a0a-3a3a-b039-370b8f60063a | -7.72044 | -45.34173 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 538ae426-56a3-3fc7-823c-8f4efe75cf38 | -9.07775 | -46.55031 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 190b70d8-2864-3ec3-861f-a3f5f7650002 | -12.81936 | -61.57821 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 127a3476-6437-3e9f-9ff3-7a45c4186bc0 | -5.73657 | -45.03334 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 55cd9f93-7e47-30f9-bd43-2195a0ad22be | -7.67903 | -54.74923 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0a9aa2d3-15c7-351c-a18f-a681dacd302d | -9.79796 | -44.82476 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 20bd41b8-67ca-3b12-8fd5-b1b97b6e9d1c | -12.79595 | -54.00313 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 7820829e-2d8d-3464-a453-d9c0990742f8 | -10.95162 | -43.87984 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 9eb8e444-d0d4-3c67-8bf1-516b8b712688 | -9.1919 | -46.95413 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4780350-6298-3372-86c4-af77f4468146 | -8.88555 | -66.81999 | 2026-09-28 17:09:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c64eb198-1c60-365d-b595-57895f0cb85c | -9.96611 | -50.14468 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| ac144962-7579-35c2-a010-d2de36b5fc49 | -10.75298 | -48.77234 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ac4a0401-b9b0-383a-a68b-04f39cb410e2 | -10.82271 | -60.7357 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 81957e31-1790-3955-b58a-4577784001cc | -8.26939 | -54.78686 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 25236621-ab7d-3a6e-9049-f078576fa476 | -11.8662 | -47.09126 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1541cbfb-dc00-3936-aabe-ce8fa606bf9d | -7.32927 | -54.99718 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 356c2a5b-e8d8-3bf7-826d-495aaa8fbf5d | -11.65317 | -50.68476 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 20afb429-dcb0-3018-8cfc-12ef8477e243 | -8.17858 | -44.43761 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 54ac5592-f858-3330-9dcb-ba750f4d03d7 | -9.08974 | -61.01508 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c0b3b50c-d676-36b6-9cf0-1cabf3d4ad54 | -9.04617 | -49.63094 | 2026-09-28 17:09:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| f584fb11-01f0-3766-a217-2400ac76cf32 | -12.84814 | -54.03453 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 06dbd821-f5de-30ad-adeb-4235dc2d4aca | -9.69681 | -54.31834 | 2026-09-28 17:09:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5b40579-82e1-37fe-89ad-e53274ea606a | -10.0867 | -50.39396 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d16a9d8d-439a-35ea-bcb5-bf03bab499cf | -8.10871 | -44.00199 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c8ec1cb6-3f47-3707-b053-05a9677570fa | -8.93027 | -45.05343 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8d169162-a216-393a-b0ed-f80f03b72eb2 | -11.8708 | -47.09045 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f2e320ee-3dc4-3d05-ae45-68576d50c316 | -11.39267 | -45.41574 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2447d01a-e83a-3f14-b0b7-83a6f11ec969 | -11.11597 | -43.32134 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 538e1783-4031-3545-81c9-b628db635940 | -9.39932 | -46.38512 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 89dc2b09-7dce-39ba-b16d-f487638c222c | -12.22266 | -50.43068 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 3e78dc7c-a2b1-31dd-b2e9-7e561857d920 | -11.54233 | -47.38988 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| c0bd3b05-cf2f-3465-a900-6c38ee9d40b0 | -12.7998 | -54.00613 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ace1b976-533f-3a7e-aa8a-3f714bcf6710 | -8.28105 | -54.72761 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 63601a8f-1dc9-3a38-97e3-3c514c297162 | -11.10102 | -51.3742 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 426272a5-f2ca-34c0-bda2-df9a84a04897 | -9.87267 | -43.62081 | 2026-09-28 17:09:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 445f750a-524f-39ec-9eb6-6363f4193c7f | -8.65694 | -45.36684 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README147.md)
