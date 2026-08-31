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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c1e9bfa-c1f7-3880-a091-4d3710cfcadf | -7.6374 | -46.73426 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e308ad8a-427f-328c-a191-3149d37abd8d | -8.92116 | -44.16901 | 2026-08-31 16:50:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7f343a99-134e-37f7-bb3b-aa3ac33bc9e3 | -11.80377 | -44.89431 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fae321bb-b37c-3360-b2b9-0a7ad7cadc2a | -7.25843 | -43.49007 | 2026-08-31 16:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d22113a5-d619-36fe-8f11-b25b05daa3a3 | -5.63928 | -44.27369 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b94eda7-daa4-3a6c-9b08-d5eb4d5c167b | -12.01102 | -60.51073 | 2026-08-31 16:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e8c0a85e-4886-3bf1-a575-691455c114b7 | -9.48601 | -57.02388 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a437416b-00a4-35b0-8aa1-b503cc7afc83 | -13.84 | -54.09219 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 15b62c90-5886-3ccd-93d7-68f01f1e4655 | -9.15253 | -59.53032 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| b1d47165-4380-3d3b-aea6-ac6edbd74b60 | -11.20025 | -50.62381 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ac5f5ad0-fc87-34a2-bc43-c0882b82ed4a | -10.13863 | -45.86459 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| a2de2656-74ca-3137-88a7-af02661a4f7e | -12.89357 | -45.83955 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 99cb70d7-92ce-393d-aef7-fc84bb8715d2 | -6.9211 | -55.7042 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 22994024-4a6a-3b14-b634-88003f2885d1 | -13.82673 | -54.02465 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e7909e5b-b543-3ff4-9b14-c88e42b72cc2 | -10.09796 | -50.28053 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4ba251ef-c82e-301a-a9e0-7159c21f21a0 | -13.47216 | -51.41279 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 442da2b3-de4d-3521-a28a-d7f2d4fd300d | -11.25079 | -45.09805 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 18084c44-5c06-3253-a31d-c0071f909df5 | -7.98614 | -46.51944 | 2026-08-31 16:50:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c9453b10-bd40-39a0-9c39-3395c7aa944f | -13.43041 | -51.70051 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| bb24dcb7-0277-34cc-b69e-ec52ee476476 | -11.49559 | -50.34752 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6e57889f-e529-39ba-b0ff-4cc62f5a973a | -9.41046 | -45.66088 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| aeb1c444-3aed-3538-8ec4-fbd5f72c6253 | -10.1538 | -45.75757 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 6291015f-1299-3f50-bc07-a2fc4a6133be | -5.59545 | -42.32099 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ca12975d-234c-3bba-804d-ee5c713cac3e | -11.63788 | -49.40951 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2bdc71db-a4ab-3537-b02c-3a0e8ab050ce | -13.48338 | -57.05947 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c1e37fbe-ddf2-3a18-b2f5-ee50cd78ddef | -12.96557 | -45.93867 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 8fcbeed7-6de1-3243-a45f-5a5fa024d43f | -8.86102 | -47.08862 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5f6a82f2-9ea9-382b-94c3-6f9230134b81 | -5.77453 | -44.13043 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 75996d4b-690d-3d6f-ad00-042c0ad61071 | -7.60905 | -44.92463 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d8e1f8e8-ba0e-3465-83fd-f769d9e39064 | -11.03666 | -47.1243 | 2026-08-31 16:50:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4187ad39-d664-3e30-ab7b-a4477764d1ae | -11.25049 | -45.10281 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bd8f57a3-9e13-317c-92e4-d4ad4e897c96 | -10.86533 | -50.48312 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7946a263-4fd9-3fef-a0fa-6fc8bfd9cfbf | -10.85996 | -45.37088 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f791c7d4-bef6-3562-9e47-845ca872cc3b | -6.73665 | -45.06803 | 2026-08-31 16:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 6accc297-5e19-388a-a6ad-97782576280b | -10.92567 | -50.6189 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 34ebc696-409e-3a13-a754-52b1efc0bb6e | -7.62352 | -57.61851 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c6e6cbea-20dd-372b-8244-bb58e907d6af | -11.21675 | -45.09106 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9c521395-92a0-3277-8ab1-3394c9fe8c0e | -8.48888 | -54.5894 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ca5265a-f468-3530-a8ce-3beb476f469f | -12.10007 | -47.14959 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a3276107-f224-36ad-a3bb-b1d60f8743ac | -10.10046 | -50.27628 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b784e181-e96b-39cd-bb45-ac43258eba8e | -7.633 | -44.83256 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| db654deb-0f1c-31f4-a0be-90ebdd9ac3a2 | -7.95877 | -43.86523 | 2026-08-31 16:50:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 864d4f23-6d64-3f1d-a8a8-ffcdaf4a38ff | -9.16166 | -60.94175 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 73b1d6fd-42d5-3e61-b0b5-740ea22a062d | -7.98867 | -44.28804 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 53af6da2-c65e-3654-938a-8930ce1d9cea | -8.8517 | -47.08279 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| be03bc15-ac60-3df0-9822-9c0a9e03559e | -13.46656 | -57.04049 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 5dd4abc4-7576-34c7-9771-dd13375cf000 | -11.07557 | -47.15456 | 2026-08-31 16:50:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0c3ccfb4-2e0b-3d71-9298-0daa4d487471 | -9.43901 | -45.6352 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6fe3036a-65ac-3c46-8329-4d610d693eee | -11.32431 | -45.17458 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| f74fef82-4a3e-33fa-b703-a0c1b7302f45 | -10.86476 | -50.47923 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 08187c21-6d09-3303-a75b-40cf37e42ca8 | -12.10785 | -45.02564 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8e933e6c-93c7-3ee1-a2cb-802960cab9c0 | -9.47137 | -48.19477 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 50bd3c0c-7625-33e9-8903-ebbb7ffa2b42 | -7.05436 | -52.71533 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| dd36cf9a-8aff-386f-92b2-168d44352d86 | -9.16175 | -45.80248 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7258a27b-97db-3dd1-b302-d3a92fe1df2e | -7.45446 | -59.93475 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 4437879a-6f83-31a7-b35b-62ae5e9680b6 | -12.10088 | -45.00247 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| d74b70bf-bae3-320d-872c-1f5948904174 | -8.76688 | -46.45341 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 03f5a405-39d1-394e-b988-3d7201b6201d | -7.02238 | -43.70528 | 2026-08-31 16:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aaaecb51-76d9-3969-8688-e5abf6076e0b | -8.10946 | -45.47505 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd7cd26f-e982-32b1-9b8f-0ef2b153086e | -10.09852 | -50.28429 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4231ceb9-fe2a-3f4f-aab0-aaaf5b11a7d0 | -9.78087 | -46.61206 | 2026-08-31 16:50:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 29e050fb-4296-3053-a355-54a581f7989a | -9.58999 | -47.60092 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 37c453c9-417c-383c-911a-ffc4023beffa | -13.47751 | -57.05655 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c72a2177-a63e-3726-a800-90dca86bc177 | -10.31123 | -49.99588 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ffdd15c0-df6f-3348-99e0-662cf5711a7c | -10.13313 | -45.89717 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 970244fc-7246-3c4a-b79c-d89659278ad2 | -11.21658 | -46.11723 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e9ae504a-4430-3c99-b521-ad53c3687292 | -13.43452 | -51.69737 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 889038ab-42d8-3e4c-83e0-e7fed34af4e4 | -8.94139 | -50.76137 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 309ca5d8-417c-31e2-93ac-460b88ecc074 | -11.23028 | -45.15203 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| de8beaba-da3c-30d4-b8c2-3c2c7eb36aac | -10.98672 | -48.38763 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 366f1180-527e-3ab9-b149-36a5f34c2352 | -10.85608 | -45.32619 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| bf1f50b3-458c-3002-a7f6-af5cdf6ed810 | -7.42036 | -44.25516 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4afd8432-a8c7-3ffb-bb52-6e5408587a66 | -11.19394 | -46.1063 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| da8c07d1-fa5b-3c7a-962a-6596ac270639 | -8.17265 | -54.92891 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| b1c95bad-7e99-349f-a366-fc8aec5aef55 | -8.812 | -49.1686 | 2026-08-31 16:50:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b4165ab2-8458-303a-8e2f-fcba3f985025 | -9.19971 | -47.99589 | 2026-08-31 16:50:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d8357512-f543-387c-9e04-d9435a4da4f6 | -10.74245 | -50.87728 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8c921257-3428-30d6-9000-56b258f3aa2e | -12.89659 | -45.83488 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 9814fdef-a699-3da9-8898-1601eaa4a557 | -7.55691 | -49.6853 | 2026-08-31 16:50:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 48d85ab8-2d11-3c1b-a5cb-c02040dd7bb8 | -13.47944 | -57.05697 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2b741f49-ba69-3f22-a5cd-cd76ddd42428 | -11.69602 | -47.6106 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b5a799c-0048-3548-b561-35450714b04e | -11.54593 | -45.48793 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 87ea0e26-cf5e-331d-ac33-b12523b6a3ab | -9.4426 | -45.68001 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 61d7aaca-c699-3e82-9cd1-04dfb0cdbe1d | -8.86662 | -47.08028 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7d193818-3b1e-3d4d-8f08-e7b090e80313 | -5.76805 | -44.11659 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 315cc5ec-c6ef-36f2-a563-8f60fa44e4a9 | -8.87518 | -46.02747 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 0e476734-f5e3-3007-b652-03859d8bfbd3 | -9.40873 | -51.65812 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 75097960-a8cf-36a9-8d09-0b3abc4b525e | -8.6109 | -54.79042 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 249516e1-be00-3235-8b26-fec3af24647e | -11.67669 | -47.61727 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c0e2c399-6afd-30ab-b4b0-f54b72bde539 | -8.80887 | -62.49939 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.6 |
| edd0156e-3266-32a1-85f3-2edc9ffeeaa1 | -7.77722 | -44.05522 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2676c9d5-ec1d-32e6-89e9-047ba4c2819a | -7.08282 | -43.61216 | 2026-08-31 16:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ca2e56f-7af7-3f92-8581-ef037c51fd7b | -6.40995 | -49.92968 | 2026-08-31 16:50:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d82a5a69-5ad8-3103-9357-bca7bbdc4186 | -13.41469 | -51.38355 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1a07c797-790e-30c4-a260-2bc2fe962b70 | -13.47454 | -57.03203 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 8999f021-9afa-3aec-a1f2-49d2c8c37697 | -6.81381 | -43.50158 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ac08ce79-d696-340e-8df8-38b760379a77 | -6.7034 | -45.03064 | 2026-08-31 16:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 31855c71-45ba-35d4-a4e3-5c440f6facb4 | -7.61876 | -44.93696 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 56d8c63d-b387-3146-bd7f-35a09f0c0454 | -11.6807 | -46.7464 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76b2c7c4-c17f-3e68-90e4-923834ba351d | -11.25452 | -51.25594 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README154.md)
