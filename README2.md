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
| 876943f7-77a0-374d-8d75-1853ae3d76af | -6.34661 | -43.65566 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 697e6ae3-0ee8-3755-b12f-86672b184dac | -6.18864 | -48.0443 | 2025-04-17 03:57:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdb0eee5-368e-3ceb-8192-2500c6e986a7 | -6.35086 | -43.65796 | 2025-04-17 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9245ba32-29b2-388b-b643-fe9578a8b0b3 | -3.96102 | -41.48287 | 2025-04-17 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e093a594-e1d4-3860-89a4-c023af9f5c45 | -6.18701 | -48.08326 | 2025-04-17 03:57:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84d6e315-05b3-3eb5-86d6-bf244392b016 | -7.24153 | -44.77308 | 2025-04-17 03:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d0063da-cdad-36dd-b9c4-d473040e42a6 | -4.14869 | -38.18705 | 2025-04-17 03:57:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 36ac5fcc-6912-3a6d-97c1-729c88444190 | -8.38947 | -35.02509 | 2025-04-17 03:57:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3b0f2bc2-f0bd-361a-8c88-60b98b4c451f | -5.6438 | -43.70934 | 2025-04-17 03:57:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53c839a7-1d8b-3e64-933e-af5b1cf9f9bd | -5.42751 | -43.20129 | 2025-04-17 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 932abc73-e8f9-307b-b89f-14a94cf3cfca | -6.18755 | -48.08016 | 2025-04-17 03:57:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6bdcfed-2fec-3bd8-be7e-230b3d62f6b9 | -5.63999 | -43.70876 | 2025-04-17 03:57:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b876d1c-7b09-30f2-9188-75810943ba01 | -5.93621 | -44.47135 | 2025-04-17 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fffd2ba6-4de7-3db7-b4a3-fc513394a9a8 | -11.67571 | -37.64673 | 2025-04-17 04:00:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1741729d-db44-3891-983d-7ecee47361e4 | -10.98314 | -44.43658 | 2025-04-17 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a266c9d-e96b-30d5-be89-aa68874ee547 | -10.48308 | -42.4265 | 2025-04-17 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f41466b-3c82-3822-9d4f-cc37e06eac25 | -10.48187 | -42.43388 | 2025-04-17 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8e184457-9a10-38df-8e02-93090ad25b71 | -13.45675 | -43.56784 | 2025-04-17 04:00:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 310e7de5-edf2-32f8-b607-d5ad55364a54 | -9.79696 | -36.94761 | 2025-04-17 04:00:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ab0caf1-cc4f-3f39-af6d-33518e489857 | -11.67936 | -37.64729 | 2025-04-17 04:00:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a548deb3-fc14-3c25-a63c-a4a1da403532 | -12.11348 | -38.0184 | 2025-04-17 04:00:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba56207c-7732-34b7-b21f-870149ad8643 | -10.48248 | -42.43019 | 2025-04-17 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ef106ca1-3b4b-37c3-a76d-24060056ed6f | -11.40989 | -42.29233 | 2025-04-17 04:00:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 366f13ff-1712-3425-8df5-5bf01dc11f69 | -10.9824 | -44.44098 | 2025-04-17 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdd61106-507a-30cb-b854-a0371663a5f4 | -14.11787 | -41.67776 | 2025-04-17 04:00:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5b57c76-02a6-3ee5-b391-a523e5188281 | -10.47848 | -42.43332 | 2025-04-17 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c40deac9-9c5c-34a8-9974-40d0349d6311 | -9.79628 | -36.95211 | 2025-04-17 04:00:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5284bbab-8767-3658-81e9-96fe006320f7 | -10.98681 | -44.43724 | 2025-04-17 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7d53885-9c83-3a53-8b73-7912db92ca4e | -10.47908 | -42.42963 | 2025-04-17 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| afd00f90-a0dc-3efb-a1d0-7c32762ef78b | -12.35769 | -39.0952 | 2025-04-17 04:00:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d9ba0113-248b-3e25-aa4c-ecee02227eee | -9.96948 | -37.26656 | 2025-04-17 04:00:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea3432a4-f44c-31e4-a6e4-fd2de67faf7c | -9.96991 | -37.26493 | 2025-04-17 04:00:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ca1731c-38f6-31d9-9d0e-a3d0125b6b59 | -13.11689 | -43.48407 | 2025-04-17 04:00:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5624017b-a691-35c8-85b1-87d3eeeecf4b | -9.80001 | -36.9525 | 2025-04-17 04:00:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59341b90-3997-30dd-8e87-6e6047ea088f | -10.47969 | -42.42594 | 2025-04-17 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c02f7fc-7764-3f67-9c47-21a023de2bfd | -12.46854 | -37.97142 | 2025-04-17 04:00:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ce966342-fb19-372b-b17f-39728bf83624 | -9.79889 | -36.9504 | 2025-04-17 04:00:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc546a45-94f5-337c-af71-876446065da3 | -21.19534 | -44.93673 | 2025-04-17 04:02:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 72022fe3-7ad5-35b7-9191-bcb8a26ba4f1 | -20.01985 | -44.59668 | 2025-04-17 04:02:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba1e8aed-6141-3a67-8289-a5da52c75506 | -19.05481 | -44.35746 | 2025-04-17 04:02:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82bb2590-5876-3ed9-b339-74ee42c2f0a3 | -19.05418 | -44.36126 | 2025-04-17 04:02:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8d7588e-667f-37c8-a6a5-64bc2577ca89 | -22.47701 | -48.35732 | 2025-04-17 04:04:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc71c395-1ed1-3c7a-8e48-be2e1be8e410 | -22.74823 | -43.27457 | 2025-04-17 04:04:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fb934269-9bdb-3a34-911e-d8dceb6be193 | -23.98147 | -48.91712 | 2025-04-17 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51785731-c25b-3778-a60f-06153e34726c | -24.24271 | -50.74078 | 2025-04-17 04:04:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dca20ea8-fb6b-3bd2-becc-678b380650fd | -23.98536 | -48.91798 | 2025-04-17 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 057182ed-c0b6-3f92-904a-841e8ae31242 | -22.5377 | -48.81301 | 2025-04-17 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c6f6ac9-9ade-3ca5-a093-f51bda9d7d12 | -22.85497 | -42.9809 | 2025-04-17 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ff2411b4-9a7c-3461-a110-ba7eb0ed0fb5 | -21.22023 | -48.6132 | 2025-04-17 04:04:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7a273119-a210-3da3-83dc-4e4541728603 | -23.2127 | -46.55701 | 2025-04-17 04:04:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9b2043ba-ff06-3a6c-acea-c91b303ff7b2 | -22.19271 | -49.66791 | 2025-04-17 04:04:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd2ede1a-a142-323a-b03f-a3a961bf2894 | -29.13375 | -51.09213 | 2025-04-17 04:06:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eadcae9f-e8bd-3485-a80e-3d5e7fa5cc4e | -5.1674 | -45.11229 | 2025-04-17 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c33e961-5e10-3acf-b738-2bf0e90a3336 | -5.16198 | -45.10767 | 2025-04-17 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f955af86-5e1d-3579-856a-0200a01ce4f2 | -3.96234 | -41.4836 | 2025-04-17 04:49:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8a9da553-03de-350d-a935-6df282926841 | -6.18678 | -48.08234 | 2025-04-17 04:49:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d86bbf0-fc1c-3d2c-80c8-e5b5a73f5f6e | -5.43039 | -43.20194 | 2025-04-17 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| daa164a6-e75b-308d-bb6a-c5bd6de675d9 | -5.4315 | -43.20344 | 2025-04-17 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dabfead-e134-39ad-8da2-e762091aad44 | -6.34333 | -43.65466 | 2025-04-17 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce98e0db-0d8f-317f-ae17-3005d424a789 | -6.19135 | -48.07816 | 2025-04-17 04:49:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d31c4df-fc95-35b7-860e-664ed67c906c | -6.19065 | -48.08288 | 2025-04-17 04:49:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7301bebb-a311-33c6-92fd-521715f81ed0 | -5.16664 | -45.10829 | 2025-04-17 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5d957b0-eeda-3a18-8ff7-b639a516ec5c | -5.94578 | -44.46977 | 2025-04-17 04:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8fa63c7f-cebd-3c92-b8cf-dea376cf78dc | -5.16345 | -45.10688 | 2025-04-17 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 966f6b07-c347-3edd-9b6f-23a2fe60651f | -6.18861 | -48.04294 | 2025-04-17 04:49:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30880284-365f-390f-8ae4-d6472e015721 | -6.34891 | -43.65513 | 2025-04-17 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aadbcc26-dcf8-3ed2-9196-3752e8562f3a | -6.71759 | -47.60967 | 2025-04-17 04:49:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7336722-54d1-3c2c-9815-6fe6946079cd | -6.34846 | -43.65845 | 2025-04-17 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0eb4a775-439c-306c-b3b1-f0ab4ee25f3f | -4.12948 | -54.89844 | 2025-04-17 04:49:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bad1bed7-65a9-3cdb-a5fd-b75256811c79 | -5.64916 | -43.70908 | 2025-04-17 04:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45655e71-a470-3976-9488-32af2a04d574 | -5.16596 | -45.11311 | 2025-04-17 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d18c0fb9-b30e-3397-9e8d-b9ba93f2caff | -6.18932 | -48.03812 | 2025-04-17 04:49:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebd1b184-8ac4-360f-9606-5286ea7c1550 | -5.16811 | -45.10749 | 2025-04-17 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d37542e-3e1d-308c-a7a0-7a270c78a043 | -5.43199 | -43.20007 | 2025-04-17 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d9def7d-9aae-35cb-9bb5-59e9d52f891e | -5.64402 | -43.70823 | 2025-04-17 04:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43e33cd2-a0c1-3e01-8c6f-c399433822ea | -7.24318 | -44.77371 | 2025-04-17 04:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d97d49a-8179-351e-8f4a-330364029876 | -6.34903 | -43.65211 | 2025-04-17 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfab4e08-b759-33a8-a263-618ead49345b | -3.69823 | -53.75549 | 2025-04-17 04:49:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d30a397-2f14-3167-b5a0-bf8a5518adb4 | -5.48249 | -43.33331 | 2025-04-17 04:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 799d38e6-ddf3-3d02-abf9-947dfa72b352 | -6.3437 | -43.65422 | 2025-04-17 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ee7b439-f221-36ed-bb9c-6e1f884214ff | -5.49697 | -43.95056 | 2025-04-17 04:49:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 040d7ac3-e7dc-3440-a851-a4cd499d770c | -6.34807 | -43.65886 | 2025-04-17 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b7f9338d-dc8c-3092-a6e7-994d65978a0c | -5.64358 | -43.71134 | 2025-04-17 04:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d6435a9-f970-325e-a8ec-293156e8be74 | -6.72108 | -47.61385 | 2025-04-17 04:49:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 294e51d2-e60f-3bc7-beb4-f906dfa178a0 | -6.34854 | -43.65556 | 2025-04-17 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de325c99-3b8a-36fb-b8fc-1bc6e2d556bb | -5.94086 | -44.46906 | 2025-04-17 04:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df3561f7-2394-3dd6-9c7c-2798e8f17529 | -6.34938 | -43.65164 | 2025-04-17 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bbdc7e5-7ac5-3d1d-9949-9806a0a2e617 | -10.48134 | -42.42831 | 2025-04-17 04:51:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b24457fe-ab3a-349a-ad92-4c85411b9cd9 | -10.48079 | -42.43287 | 2025-04-17 04:51:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0b631c8f-ba23-3bbb-9e5c-f3f8bcf6c7a9 | -12.97917 | -55.16746 | 2025-04-17 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f126c013-1d5a-3e78-b361-cd52a0c9b1db | -14.31321 | -59.89506 | 2025-04-17 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9960e341-d9ca-3448-ab15-86572182468b | -21.46582 | -57.16119 | 2025-04-17 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94472322-f948-31ea-a321-65ae38f1a4a1 | -21.22358 | -48.61481 | 2025-04-17 04:55:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| abaf2ca8-8af8-33c1-8027-63ec6c93a338 | -23.33909 | -46.77139 | 2025-04-17 04:55:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 78fa0f6e-075e-33ab-bcef-646a49ecbc25 | -22.54098 | -48.81166 | 2025-04-17 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a617aa7e-b287-35a4-a9c1-83d5429a63ae | -26.46696 | -53.4931 | 2025-04-17 04:55:00 | NOAA-21 | SÃO JOSÉ DO CEDRO | SANTA CATARINA | Brasil | 4216701 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d95a99df-1aa6-3594-99f8-419523e6a9b8 | -22.75478 | -43.51825 | 2025-04-17 04:55:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7f07695c-2ab7-336d-aeaa-93f6307c15a8 | -6.34339 | -43.6497 | 2025-04-17 05:14:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2a5b85d3-68d3-37c4-8b76-b23b581bab2f | -5.93882 | -44.4645 | 2025-04-17 05:14:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9b2a5798-4460-34fe-b8ed-7f2d4ee8cced | -5.42587 | -43.19733 | 2025-04-17 05:14:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README3.md)
