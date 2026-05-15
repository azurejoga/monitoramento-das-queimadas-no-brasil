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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 132e3322-7526-316a-ae64-0601d95a1305 | -9.46152 | -40.33669 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f5d039f7-c606-32e4-9ba2-6219657cd03f | -14.98365 | -49.56791 | 2026-05-15 04:17:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f0ea2a1-b010-3716-b14e-17a3bdd0d5b7 | -14.23099 | -45.44044 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39437c16-0fd2-3170-ad1c-bb38e237856b | -8.72445 | -48.32955 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac352ea9-59ba-304b-867e-cceeaf978504 | -14.33308 | -45.54439 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82e4dc1b-76f6-38ab-8a3a-d1ea3976ba57 | -9.3082 | -45.48528 | 2026-05-15 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a52bbf9-e711-3552-958f-9e98bcabe566 | -8.08793 | -44.15916 | 2026-05-15 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38c97deb-531c-30ac-8d6d-b1d2d2285f5a | -13.95566 | -46.02919 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc00e335-9573-30f9-ab4b-b38e5fc43e24 | -6.63934 | -44.49117 | 2026-05-15 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd1437e4-45c6-39dd-b4ff-0da372f26c06 | -8.55064 | -45.98753 | 2026-05-15 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07f1c2b6-9ad8-3c23-ac1a-cf6f0a9036d4 | -6.96877 | -44.54974 | 2026-05-15 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e92a91d-8811-3637-a9c0-5f4e67e4457d | -9.47189 | -40.3383 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.3 |
| a0d3d19a-057f-38a9-b0cf-a2fcd0d12d7c | -15.05612 | -42.95574 | 2026-05-15 04:17:00 | NPP-375D | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 681446ae-57c3-3134-86fc-77392c7a90e2 | -8.96677 | -45.672 | 2026-05-15 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f98a53df-594a-3c31-aa88-02ce68bb0c5e | -14.23253 | -45.45251 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a785d6ad-3a25-3463-a200-3251b673a5ff | -12.49854 | -43.7696 | 2026-05-15 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 248ba3f6-ef7f-3322-aa14-6b41033cf9ec | -14.22566 | -45.45129 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a57e8f13-c91e-3403-9ed2-3c8d19f23050 | -13.95849 | -46.03382 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98319100-8eb8-3166-96c6-e5b44a58ca69 | -9.46786 | -40.34156 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 1d80f366-9bf6-3520-912f-57d78ba13d60 | -9.46901 | -40.33397 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 6738729b-f72b-365f-ac0d-d6553a213b83 | -9.46843 | -40.33776 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.3 |
| fd36bcc2-6f9b-33c3-b92b-246855c56a69 | -12.47562 | -45.44042 | 2026-05-15 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb4c01a9-7571-3c3c-afdc-f23cd8606a78 | -9.46555 | -40.33342 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8840e7c3-9eb9-3e5c-8145-2a352d3a62fc | -14.22909 | -45.45189 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a3563ab-537b-3788-b8b0-76b8ccaf153c | -8.54986 | -45.99209 | 2026-05-15 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48d341eb-cc4b-3364-8fc8-cae0a2c3a207 | -15.11271 | -43.96914 | 2026-05-15 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1546b3af-09a3-3960-be98-dcc64270d722 | -8.5447 | -45.97718 | 2026-05-15 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c180f6aa-d615-34c3-bf42-08aaf79bc727 | -8.72806 | -48.33443 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9a9f943-4cf9-34ee-9ebe-df28ad329cd0 | -12.48325 | -45.43768 | 2026-05-15 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dd137f4-c1e9-3563-8446-f19c1ed25d98 | -12.6017 | -44.50914 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 264b16aa-cd6d-3164-badd-037fe389f8c6 | -6.95588 | -44.53949 | 2026-05-15 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cae7ba19-d265-3650-b58c-85e695a4e9f1 | -12.50188 | -43.77015 | 2026-05-15 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cdc7f46-b4e8-3e9f-86ad-1ee18e1bb77b | -11.93664 | -47.8836 | 2026-05-15 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7ea651a-834d-3a22-a0d7-3a05d466400a | -8.71939 | -48.33295 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dbbc2fcc-caf3-3803-9e73-6cd10d47b82d | -12.21676 | -46.57962 | 2026-05-15 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21a2c100-d536-3acd-9d8f-d7a25da36d84 | -14.22819 | -45.43601 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19786ba3-ca09-33b8-adbb-a8b4ed3b556c | -12.4791 | -45.44102 | 2026-05-15 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02990b62-6f78-3ec6-a764-7670f62bf062 | -6.94066 | -44.2828 | 2026-05-15 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54f78a25-1f6d-338e-8ade-bbdbb3842ba8 | -9.31112 | -45.49008 | 2026-05-15 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0935950-bd12-38fc-9d5e-8f56bc5accde | -9.3075 | -45.48945 | 2026-05-15 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c43934c1-a7f1-361e-a1c9-4fd5ab1da8cb | -8.70403 | -47.97775 | 2026-05-15 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da47ffe0-5638-31b2-9cd1-b6036940e235 | -12.72658 | -41.80602 | 2026-05-15 04:17:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4ddc3c5d-1bc2-395e-8d40-f35844e52329 | -15.11604 | -43.9697 | 2026-05-15 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f95ea4b2-af1d-39b8-9416-121a1a9ef19b | -14.03825 | -43.85199 | 2026-05-15 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 62f28561-efb6-3496-b0a8-51dedb7bb768 | -12.60568 | -44.50605 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cec13cd-bbcc-38a8-b283-82995c33f8b1 | -9.47131 | -40.3421 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 7e3d40eb-5f2f-315c-8c3f-a2cb3ea9744e | -12.50131 | -43.77372 | 2026-05-15 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84df38fd-3de7-3d6f-8f50-1644cbda79fe | -8.54766 | -45.98237 | 2026-05-15 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55574775-3c09-3a89-bdc2-cc7437789d49 | -14.33652 | -45.545 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb1e6dba-8404-3007-bf0a-583b46733573 | -14.17422 | -52.86782 | 2026-05-15 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6edfb41-ceb2-3d37-b984-e11d2fa4c11d | -8.54392 | -45.98173 | 2026-05-15 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 59d81601-7358-355d-829b-816cdc5ab47a | -6.39103 | -44.17981 | 2026-05-15 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dffa11c-c457-3cf1-be38-e2bc7887043b | -12.48173 | -43.78875 | 2026-05-15 04:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de759bce-2a14-388c-b9cc-a87a2a7e68d5 | -12.61244 | -44.5072 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68236670-28ca-3407-8e3f-a9768f6b86a3 | -8.69979 | -47.97707 | 2026-05-15 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88d3df1e-aaf8-35e6-ba94-87bb59f47eca | -8.7047 | -47.97385 | 2026-05-15 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecb96263-b7e5-33b0-9376-eb0b1bbdfd84 | -8.96894 | -47.25352 | 2026-05-15 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c9a4770-f85e-37f9-82d7-6f26e0460f61 | -12.84954 | -43.75758 | 2026-05-15 04:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4a855fd5-abc0-38aa-a03a-0988ecb7470b | -6.38816 | -44.17532 | 2026-05-15 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68562389-4126-3a1e-971c-de50ab761aa7 | -12.60846 | -44.51029 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c66b9f5a-403c-3360-a2b4-728dc222d010 | -13.67862 | -42.7303 | 2026-05-15 04:17:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d85432e2-6f53-3290-90b0-997785bd8c53 | -8.72516 | -48.32545 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b87105d2-63ee-38de-8648-16d014513b22 | -8.72372 | -48.3337 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 09980814-ff80-32d1-a75c-e5c7744be75f | -9.30099 | -45.48401 | 2026-05-15 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0398c1e-1178-3916-883a-3a920cc0da3b | -12.60628 | -44.50238 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12b2d08a-905f-381d-979d-13bb442d62aa | -8.50243 | -46.38496 | 2026-05-15 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 111c7a50-170c-3d81-9da6-731512acf65e | -9.4644 | -40.34102 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a4abd387-379e-3c08-b6cc-ab89c1b2aa62 | -8.50163 | -46.38969 | 2026-05-15 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cece7532-a36e-3213-a820-fd7ba03fd32f | -6.39167 | -44.1759 | 2026-05-15 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9120f20d-8794-34dd-9631-bee34544d3dc | -12.59832 | -44.50857 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24220ca2-c4b6-3e7c-a682-bca38798e76f | -11.97964 | -46.79328 | 2026-05-15 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c04f5816-c638-3920-8420-3886cbc7bf28 | -12.21383 | -46.57452 | 2026-05-15 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac0aa1a8-5503-34b8-b640-6a82d7b81b64 | -8.54689 | -45.98692 | 2026-05-15 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee7f6d75-ddc3-39be-8c57-73f94725baed | -8.723 | -48.33784 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aa65539-235f-3253-968c-c75169b7e5ca | -14.08371 | -42.11687 | 2026-05-15 04:17:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b46e4e00-337b-390a-ada4-315dcf5858f9 | -8.81743 | -44.79121 | 2026-05-15 04:17:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a76f2f66-a537-3675-a6a1-9fd9c9cb0b3d | -14.17955 | -52.86882 | 2026-05-15 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e7f15a4-c955-3fd8-bb3d-ead31319ba73 | -14.21128 | -45.45269 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2aaee4d9-e503-368c-a076-db4b66f9fae9 | -12.07669 | -51.25802 | 2026-05-15 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dc28114-7175-369a-86c0-d81eda6ef713 | -14.21065 | -45.45651 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59f4155e-c8e1-3b73-afa8-551835141151 | -13.03286 | -49.93274 | 2026-05-15 04:17:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac9bf334-d076-37b6-a818-1227458b4bfc | -12.6023 | -44.50547 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ef4c289-d8b7-36f3-8303-85bf2204875f | -8.72083 | -48.32473 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bfabd67-7189-3e0c-99ba-587cb1f5edd7 | -12.07778 | -51.25227 | 2026-05-15 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c16e9c5-bf4a-3a13-a5f0-dde5a8409f4f | -7.13237 | -44.06287 | 2026-05-15 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a1293ab-e70d-31a2-ae69-d0a60e2a700d | -13.04893 | -43.86426 | 2026-05-15 04:17:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c21a692-8550-3264-bf0a-d2de5ee9bec0 | -12.47976 | -45.43709 | 2026-05-15 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f217970-eac6-34d6-8543-78851a6d2697 | -14.20568 | -45.44384 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4b638a9-9c35-33b1-86e5-bba14b6d4dff | -14.22693 | -45.44365 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0961691a-6f87-375b-91fc-8fda28826c60 | -8.81548 | -44.80315 | 2026-05-15 04:17:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a4872bf-9e54-38cf-bb4e-3081bc28fa4d | -13.03477 | -49.93588 | 2026-05-15 04:17:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bec56f2-bd67-3594-a8a4-60011c3bedf6 | -14.20288 | -45.43942 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 916a27fb-8608-3a80-b11f-e5b3fafd4703 | -12.85288 | -43.75813 | 2026-05-15 04:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6769035d-3f00-340b-95d2-b3af87ada5de | -15.64533 | -47.92826 | 2026-05-15 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a28e22df-b790-3367-9775-b8e72fa25d82 | -11.1284 | -45.13899 | 2026-05-15 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cbc9851-ba63-391b-ac74-b5b4745c3c9d | -11.12684 | -45.12672 | 2026-05-15 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 58b8f278-935c-3e3e-adb3-a4b5c571f98b | -12.04724 | -45.28133 | 2026-05-15 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e4ad72d-32e0-3b84-9f86-a06e2324423c | -10.49757 | -42.40715 | 2026-05-15 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e840e16a-a3ad-3329-982c-8e965e59e0ca | -11.86807 | -43.86304 | 2026-05-15 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c730cb9e-3868-3e94-a9f6-0b93ff75a1d8 | -9.45709 | -47.82532 | 2026-05-15 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README4.md)
