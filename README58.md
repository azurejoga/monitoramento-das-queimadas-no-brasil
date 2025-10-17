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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1625c22-e524-37e2-9a22-dff14ca84d32 | -6.39855 | -46.87764 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c97646bd-d92e-3869-b973-e8b74409b47a | -6.75535 | -42.37654 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| af7759d5-1585-311b-98fc-5bf1ec18a607 | -3.50148 | -52.48663 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| cbe42a90-98e2-325e-b0fe-6e5f99a4ebca | -10.41718 | -48.88251 | 2025-10-17 04:19:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6deb4969-8884-3294-aec4-2505b072289b | -5.83867 | -40.81662 | 2025-10-17 04:19:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0db14b07-ccd7-370c-ae27-3bc5e8c749b5 | -5.39664 | -43.68637 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 031f33d0-8911-3103-8332-7e1086e91da9 | -5.69438 | -43.5429 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b9a9469-c9ac-3a31-8260-8f8887193d08 | -6.43923 | -43.38757 | 2025-10-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b84dcd3f-3a80-3560-acc5-8a6beb978f99 | -10.05443 | -43.86281 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 317c4876-f74f-32d6-b4c7-db671e099dee | -11.46568 | -44.24257 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84a3917b-1c8f-317c-a93b-2237f5d2f053 | -5.25906 | -50.97838 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 195f3b5b-36e5-358d-a99c-b60cc078e5a9 | -7.62132 | -47.83992 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 428e95ce-f906-302d-9a1b-e8dd47fda369 | -6.72159 | -47.20767 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8679260-4807-3bf3-81b3-82b4dda241c4 | -5.3504 | -45.96748 | 2025-10-17 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f98d6c7d-7226-39e7-b1f1-c5515bf797c1 | -10.57162 | -47.43799 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53134d71-241a-3701-b063-95c3837f6734 | -6.58968 | -43.93316 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a345981d-5060-39b4-957b-1f144a6ffb34 | -10.91169 | -47.44394 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf994c5a-fa6b-3751-9690-c9dce4852f84 | -11.49649 | -44.06245 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d11b611f-4af4-3ece-b9b8-a5a5d9421ca1 | -10.49517 | -43.37949 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 191ae594-ffc7-35df-9282-6dd1b6bc8dab | -10.28476 | -44.05099 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b936a1e-84d6-33b0-956e-f7fb524372f5 | -9.13564 | -46.63775 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95b228ca-2658-3aaa-8bf5-4256f38f536d | -8.69805 | -46.98239 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75353f69-a51b-3eec-8fc2-5047549fc317 | -8.45883 | -46.24666 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 472e21c3-904d-33e3-9bac-5b4e6b21efd3 | -8.21622 | -45.04917 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b6f9dd9-76d3-313f-b1fa-d2098ba38a28 | -7.35356 | -43.85496 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a001f853-5ec5-3fa2-b087-1164f9a8ddd4 | -8.27581 | -43.35697 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f76c1371-5d0c-3764-b01e-f0859fac0c3c | -4.50212 | -50.22196 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7507ff01-0250-3090-93b9-761ba810c10b | -9.24838 | -44.38076 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0edcd53-84ad-340f-97c7-7e79fdd6fb9f | -4.54049 | -48.4079 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2ec62a1-2115-36c7-9bdc-c109bd691770 | -7.15913 | -42.66864 | 2025-10-17 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1907a3d6-90cf-39e9-b8cd-710f457592aa | -6.26493 | -43.89996 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b9872fe-f7b6-3f7b-8766-fc4900a58290 | -6.23423 | -41.54381 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4ee7f2c-a10f-38a2-be7f-532c81ba87b8 | -8.41302 | -46.2795 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b2f0b03-1fd2-3204-bf58-8515ff6bb1b9 | -10.29143 | -44.02988 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e418929a-7c25-3eb6-9294-6abc97bf9b3e | -7.53255 | -44.28057 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e6de920-d077-310c-b709-6cf0103fbf8e | -10.50158 | -43.43042 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 58d041fd-31d2-34b9-b6a3-55b1c25fceed | -6.53732 | -44.68673 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff353b25-3497-34f4-97cc-85b65cbe757d | -5.9112 | -44.74953 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| acffd80a-24a0-3f9e-a378-3cab76b06dfc | -5.88557 | -44.82668 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f45f7643-12e1-36af-bb6e-da23a5a34aa8 | -7.84208 | -45.45773 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e29aa274-b519-34de-b13e-256cfe69bc6d | -4.01169 | -44.18843 | 2025-10-17 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42278633-6987-3dc7-9ef6-ba52a63f7a49 | -6.27966 | -44.02313 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d92c0688-35a5-34bf-9b8f-7283a4120616 | -5.91282 | -44.73921 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bcc09de-75c6-3ab6-93fd-831bbfa30be8 | -5.88212 | -44.76263 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09979f54-6622-37d1-aedc-6729d0cfaf72 | -6.26 | -43.90984 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a97d6bd-8375-3087-a693-b5f7c530e560 | -8.40856 | -46.28607 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| dc0438ea-9999-3927-ad3f-fd681d4c3011 | -10.14524 | -44.53947 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9f47001b-da70-3308-9708-45332fbbe32d | -6.35904 | -41.4857 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 38f3fb0c-0f5e-3468-adea-508accee8729 | -7.66781 | -45.6325 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e475305-3d7a-39c0-968f-069794071789 | -10.92211 | -47.87329 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82e71862-7ed7-3445-b92c-e5acea0f0226 | -6.31805 | -40.94434 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e6f8898b-7fc3-3fa1-93c2-661824e9c8e8 | -5.24346 | -50.96202 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8a8647c-8435-3d19-95a0-03422a1cffa4 | -7.96675 | -44.091 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ab153b5-0ddd-36c2-858b-789b34ea5008 | -5.73787 | -44.98668 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8132c11-066e-3f91-ae7f-90f47a600b33 | -10.29423 | -44.03407 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4172e55c-ba65-33c4-86f3-383121ab69cf | -7.27281 | -42.93833 | 2025-10-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6e9eea24-c835-3368-8003-83d9797c92f6 | -11.45746 | -44.04499 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caddac70-123c-36cb-a025-3cef5efa5e6b | -7.27927 | -42.31782 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9e215213-8526-36a2-bbe8-71f1894c0702 | -11.39312 | -44.22001 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a23f88ed-c9ee-34f0-8ab2-a884243fc49e | -10.49983 | -43.41868 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af2caaa6-8bb2-3909-8732-c6ad5de40b3d | -9.27093 | -45.26736 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ffbead57-892b-34ea-b9b5-daeef33a8618 | -10.59368 | -47.38826 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5f5e613-b105-3b3b-9b2f-d5282ce78757 | -6.21378 | -47.88255 | 2025-10-17 04:19:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6836a7cb-d049-3611-a28b-94e010b5eff2 | -10.10247 | -44.61961 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31400a41-2a5d-33d7-9cf1-66b6147cf959 | -9.1412 | -46.64605 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aa44f5e7-e6fb-378b-a1a0-3a170a0a50c2 | -9.13785 | -46.64549 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 46937106-f917-3863-82f6-01a2cf44673b | -6.215 | -44.76608 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4787abfb-d694-351b-81b1-60a76369ec3d | -9.30698 | -47.67275 | 2025-10-17 04:19:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5be64dfa-5e18-3faf-bf9e-d3a8312c57a1 | -9.14193 | -46.59834 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a23c3db-4297-3a7f-8396-e5ae66c48ee8 | -5.69855 | -53.64155 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 309809ea-2846-3614-b505-f0c97c747706 | -3.50934 | -52.49179 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9128f8fd-f933-39c5-b1d0-ef4104138a0c | -8.16155 | -47.97858 | 2025-10-17 04:19:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39fb5cea-dc9a-3c5b-abc5-035be31c702e | -10.92759 | -45.41904 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eea316b-d537-365f-b134-9b26f29c46ca | -5.46137 | -44.6461 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15c8deab-a0bd-34b7-8b02-d9421bb3a2d4 | -4.51079 | -46.00652 | 2025-10-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2d4ee532-1888-3f9a-8cd7-07971ba77ca4 | -6.21445 | -47.87834 | 2025-10-17 04:19:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c138aa6-1604-3269-bd4c-adee7bef994e | -10.91996 | -47.86493 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a486600a-a3ba-3990-8ae1-bdc82f1cb62e | -6.29842 | -45.53181 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 982e9e06-cf43-3448-b722-cf8386484596 | -11.38463 | -44.20744 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eea5af62-d7d4-3f78-bc0c-dd7032eafbec | -6.44032 | -43.3805 | 2025-10-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0341d41d-635a-3626-895d-8df41e2c65cd | -10.38959 | -45.11797 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57c69580-6fe0-38f3-966e-697b8c3eb7fe | -11.40827 | -44.21111 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 632e221b-46b1-3d52-96b4-3d30cdc6f5ae | -5.7168 | -44.51399 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b5349ac-5b20-365c-88ed-8d1cf93c8d77 | -5.3313 | -42.89899 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0745d2c-020c-30ea-90da-67c5ea268e0a | -5.32741 | -42.92422 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 071bb8cd-5e4d-333e-9d3a-ad1084a70b5c | -4.81495 | -43.20224 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bed19664-46a7-3044-b111-1343eec9e618 | -6.29506 | -44.0113 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c14d6301-2b20-3976-9c57-a5e1351418ec | -6.29786 | -45.53533 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5deb420-97bd-3345-8a39-2e3c2e2a524c | -8.25699 | -44.06012 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 648ee9b1-d049-3d33-9fa3-b49998d4a74c | -6.97014 | -45.31076 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f5db282-b77b-3850-8cd4-79a36fdf296b | -8.2552 | -44.02727 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 362822ad-deff-3d92-b2da-ccb38d6e7264 | -5.37158 | -42.72735 | 2025-10-17 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5f65413-fabb-3e72-a9a1-42de8bc6062b | -3.698 | -49.56533 | 2025-10-17 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00f5ca7a-9e95-38db-afb2-e43f8ce2d0f9 | -11.38911 | -44.20062 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16a7130d-386d-3734-af01-ca048f313875 | -5.68585 | -42.69281 | 2025-10-17 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7e0d77db-eda8-3aef-af25-1a2e005c826c | -6.73636 | -43.07153 | 2025-10-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80ac9961-e360-3c11-8d52-dff8e514698f | -6.92222 | -44.09189 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77e21d85-1cf9-3f23-b066-7f5c72e5adf7 | -9.67627 | -44.51681 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b185f82-6d13-3950-a93c-f7b488cfd3bb | -2.51672 | -51.93149 | 2025-10-17 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13d887dd-7d63-3ff8-ac7b-5e8ad2b2a474 | -7.47128 | -41.51606 | 2025-10-17 04:19:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README59.md)
