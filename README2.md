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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cc3aa65-0983-31b1-9c6b-fbea52db349a | -6.199 | -44.3924 | 2025-07-21 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 858e05e5-edf3-3c67-a3b0-f20ec3104a7b | -7.55695 | -44.55439 | 2025-07-21 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2785056d-2735-3ac1-8161-b0f057c48f0e | -9.63886 | -40.5983 | 2025-07-21 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 448a4d6f-03ab-38ad-86e6-595b17c17cd1 | -7.75339 | -42.16117 | 2025-07-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea3008e2-973c-347f-a3d1-a92f860cb10f | -7.75272 | -42.1649 | 2025-07-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a3c78c54-ff12-3c53-9dd0-b95a639afafb | -5.2685 | -44.87133 | 2025-07-21 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0282248-4454-3667-89bc-766fa243491e | -5.87072 | -45.19909 | 2025-07-21 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a88fc8ba-7fc9-351a-8b18-2cb9a3852807 | -7.7598 | -42.15895 | 2025-07-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b69ba08-31cc-3285-99c6-0df860eba9f1 | -7.75433 | -42.1579 | 2025-07-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3b364211-5049-30d6-8dbc-0083af6d1453 | -8.52068 | -41.19602 | 2025-07-21 03:30:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 27e7fc37-029a-3210-b102-2057966b8a3d | -7.25665 | -44.28462 | 2025-07-21 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2755311-8bc2-353c-a330-f1676f4a1e81 | -6.19835 | -44.39362 | 2025-07-21 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6520d8da-8ef0-3693-b5af-92ad51d763f3 | -9.63313 | -40.60274 | 2025-07-21 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b4a280d-4511-3cfc-ae47-c93cb5c37ffb | -5.28234 | -44.94905 | 2025-07-21 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 03894fc5-44ba-3e86-abd9-3554387671ab | -5.25916 | -36.99639 | 2025-07-21 03:30:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3648f422-2ee9-3347-a9cb-1a4dec22192c | -6.19996 | -44.38723 | 2025-07-21 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 249f5254-09b8-3ef3-a468-8ab5fc4eb0b8 | -7.2576 | -44.27941 | 2025-07-21 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 190e51ea-1438-32cf-b32d-0eeb62458ce9 | -7.75296 | -42.16532 | 2025-07-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 27dd1443-6be9-3d26-95cb-905928a352a5 | -7.95089 | -43.97778 | 2025-07-21 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6ec8645-caf9-3cfe-bf24-2b6a60bbe2b5 | -5.86963 | -45.20503 | 2025-07-21 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44b24778-a988-3254-8030-66638a897995 | -7.75365 | -42.1616 | 2025-07-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 691e5cc7-74e2-36ac-9131-d6ca235322cb | -7.95802 | -43.97402 | 2025-07-21 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aff2c6f1-3fd4-3871-b71b-5957bd98e7bf | -7.55533 | -44.55483 | 2025-07-21 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f753590-884d-33dc-802c-3015f351255b | -6.69662 | -45.70111 | 2025-07-21 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b92e5bc-2c4e-30d0-8561-9b072df4cd11 | -7.25474 | -44.29507 | 2025-07-21 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8d269dc-ad75-37e5-af87-f2fbb0447def | -7.25281 | -44.28606 | 2025-07-21 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa2070eb-f9c8-3346-bb79-fc78371b104b | -6.88892 | -45.39702 | 2025-07-21 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a17f31dc-6e31-3dbd-bb1a-a0bed98ba97a | -6.19928 | -44.38836 | 2025-07-21 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3dcdf51-ad1b-3b8c-9ad0-588289c27cc6 | -7.06195 | -43.51362 | 2025-07-21 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| be531e94-b835-3430-837a-4b454b103d1d | -7.75951 | -42.15854 | 2025-07-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4ec4735-3082-38da-bd60-be0a39d1709a | -6.69532 | -45.70818 | 2025-07-21 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec0eec8a-02bc-35e9-bac7-834cbffee836 | -6.69582 | -45.7018 | 2025-07-21 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 950dc714-b0d8-3536-9451-149f0028dfeb | -9.63792 | -40.6036 | 2025-07-21 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 91396b4a-737d-3f2b-8e36-ee714c635179 | -7.958 | -43.97374 | 2025-07-21 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bed1ec97-eceb-3294-a4a8-490d7b10ba90 | -7.25819 | -44.29213 | 2025-07-21 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d4dcd21-6b5d-3db7-800b-4e3c3468101d | -7.75886 | -42.16222 | 2025-07-21 03:30:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa0f43e9-b796-327c-a08e-bb4c83242939 | -10.66722 | -46.77569 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 804a61b9-92ea-3705-a683-1db5030ca4d9 | -12.46386 | -46.92308 | 2025-07-21 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad30d30-2c68-3750-828a-5080e5495b86 | -13.23793 | -41.97636 | 2025-07-21 03:32:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd09e0bd-cc7e-306e-aaf2-4b9f040a29ef | -11.78829 | -47.55116 | 2025-07-21 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8442edb7-6e3a-3802-94a2-0d6f75030888 | -14.76786 | -47.98585 | 2025-07-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57079982-eaa3-30a3-b61e-43660546d4df | -11.9608 | -47.02871 | 2025-07-21 03:32:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db6ef6c4-7507-3bfd-8e84-4bc8cf895cf2 | -10.66715 | -46.77845 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 01b68356-0435-381e-b322-66a1e0d29ce7 | -16.07627 | -43.63059 | 2025-07-21 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46f66c80-c9ae-3438-98ed-26cbfc5577dd | -14.67776 | -42.48347 | 2025-07-21 03:32:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 656c255b-a0ec-337a-b2bb-d3eb97778d73 | -12.48163 | -45.87655 | 2025-07-21 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 12cb17e1-d32f-30c8-b255-528c4c090f1f | -12.77866 | -38.50009 | 2025-07-21 03:32:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 81edbcaa-f755-3e4e-a20d-61554e6071fa | -12.46913 | -46.92311 | 2025-07-21 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dcbbc2fe-711e-3439-bc39-931b30eea9a0 | -11.79149 | -47.55494 | 2025-07-21 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e4287f6-db69-32da-89ef-07f883202370 | -11.78437 | -47.55371 | 2025-07-21 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 930ffd2f-0e5f-331d-a211-c282a74f1d6f | -11.7869 | -47.55787 | 2025-07-21 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3a9c3956-4d96-3118-8866-554087f3d347 | -11.95406 | -47.02606 | 2025-07-21 03:32:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 57a09cf8-e474-3110-b715-da20cd919273 | -10.68237 | -46.77192 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 300182a9-5e3c-3508-a79b-57a4e5de9c14 | -10.68927 | -46.77331 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6649a3fa-5736-390b-82ea-111714eb494b | -14.77537 | -47.98695 | 2025-07-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ccff088d-a560-3126-8fe6-9e4b583b646a | -14.7739 | -47.99363 | 2025-07-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 959bb320-4b30-37c8-b8c0-114e4c93f7f4 | -12.4706 | -46.92455 | 2025-07-21 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 017e0860-2389-3ac3-85d9-22460f079365 | -10.6684 | -46.77219 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61f33e18-cfc0-3659-9445-735a4cb15b7e | -10.67418 | -46.77682 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9d22b232-f3c1-3585-bbfa-38f5098f0db1 | -16.0808 | -43.63492 | 2025-07-21 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e5e7bfd-3e5b-3c19-87d2-63886f926b80 | -10.6589 | -46.78373 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49f44429-3f13-365e-bccf-8674f1106147 | -12.48054 | -45.88181 | 2025-07-21 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f3ba0dd7-e0e1-381e-80af-9c3ada1d220d | -10.67534 | -46.77337 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f20a584c-3f46-3d75-921c-dc143e720ea4 | -15.80157 | -43.32113 | 2025-07-21 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 259fece5-d9f8-3687-b4f0-80d02e96acb9 | -11.9622 | -47.02219 | 2025-07-21 03:32:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52ffa90d-e5f9-38a8-9b0a-b9a870cf55b1 | -14.77312 | -47.99451 | 2025-07-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b319d9b-95ec-3d68-aad3-466bfb5998be | -10.65895 | -46.78091 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0c16f645-53b8-39af-9bd9-a95a45750b9f | -13.49301 | -45.50558 | 2025-07-21 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8464cb33-7e5f-3568-91f6-b835d8ff74d4 | -11.9609 | -47.02754 | 2025-07-21 03:32:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0516704e-cb47-3878-a733-360c0bb80150 | -13.4925 | -45.50749 | 2025-07-21 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5aa07e05-3900-3083-9c28-bb62b62360b0 | -14.77467 | -47.98766 | 2025-07-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 077ab79c-cd37-372a-bb82-6f24a77d594e | -13.48697 | -45.50397 | 2025-07-21 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a6ad82a-4cc6-3545-97e8-3da69848ddf9 | -10.64779 | -44.48742 | 2025-07-21 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21cd2f8a-5ec7-3276-92c6-047cb18fb8c9 | -10.66018 | -46.77734 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d7c46900-4004-3c33-a905-dd5b16ffb688 | -10.67545 | -46.77063 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20cd6e19-542c-3b51-874c-aefcbeccd7d9 | -10.6659 | -46.78208 | 2025-07-21 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c8df3500-c027-32fb-87b1-9259d96e3b96 | -10.64867 | -44.48288 | 2025-07-21 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d4902cd5-298e-3d5a-a5ad-619c0ae06f51 | -14.76859 | -47.98497 | 2025-07-21 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d2bf0f9-53e2-3276-95eb-bfe98393789b | -13.63384 | -45.53157 | 2025-07-21 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e735adc-8e60-368f-a623-03fd3ceb3e7b | -23.22558 | -45.99302 | 2025-07-21 03:34:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eb36ee5c-56ce-35ee-a393-7384c34a049f | -19.17886 | -45.45656 | 2025-07-21 03:34:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5643ffd-e885-33d8-bb4f-15577115297b | -20.67012 | -44.49852 | 2025-07-21 03:34:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dc8a1b01-578f-34ef-bda4-99377b4ae894 | -23.43891 | -47.42945 | 2025-07-21 03:34:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ed134dc-8fac-3ac1-9f43-17feb4d3869f | -17.33718 | -44.89802 | 2025-07-21 03:34:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 818c0f63-b51f-305a-bb60-a9c0d62cdbc8 | -20.45626 | -45.55312 | 2025-07-21 03:34:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 573bddbb-152c-3b1e-bdb3-4d3c5cf054b0 | -23.57482 | -47.19132 | 2025-07-21 03:34:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e141d223-75e1-35b8-8c33-82a855466dd1 | -20.94752 | -45.82756 | 2025-07-21 03:34:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04063f4c-2609-31f1-b3bf-b158f662a907 | -17.33799 | -44.89419 | 2025-07-21 03:34:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03fc4466-581f-30be-8fe2-bbf36e1c2476 | -17.64537 | -44.7383 | 2025-07-21 03:34:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b0a0769-f649-39b7-9d71-f2f7505b1b3c | -17.83101 | -41.96391 | 2025-07-21 03:34:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ea0be269-c35f-3798-8b2b-da1ed6fba069 | -17.65074 | -44.73967 | 2025-07-21 03:34:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c00fec72-2134-3a06-8934-a29e80fd312b | -17.91236 | -47.76921 | 2025-07-21 03:34:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9103601-ae69-3edf-82b2-18e379b1c8aa | -20.66895 | -44.49898 | 2025-07-21 03:34:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6f1130da-877e-385d-81ec-bd07c924cdea | -19.3412 | -40.83708 | 2025-07-21 03:34:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f60c369b-6902-311d-9732-eec77f933ab1 | -19.48551 | -40.65305 | 2025-07-21 03:34:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fc4e13c7-aa08-340f-ae1d-2d36b607ecf2 | -23.27096 | -46.40346 | 2025-07-21 03:34:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a80c20ad-6d45-3f51-b03f-fdee6a869ce9 | -23.22482 | -45.99642 | 2025-07-21 03:34:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cf8abc7a-f17e-3ba4-bc13-22e763a6517d | -17.91361 | -47.76377 | 2025-07-21 03:34:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c6629c8-9f0d-34f6-bf64-377ab2c91e6f | -28.90891 | -49.96927 | 2025-07-21 03:36:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 83690be3-597f-360c-a4f4-451fc8722027 | -24.54751 | -50.79553 | 2025-07-21 03:36:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |


[Clique aqui para ver as próximas entradas](README3.md)
