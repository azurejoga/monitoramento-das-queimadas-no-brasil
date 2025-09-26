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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| badbd2e4-89f7-332d-99f8-f40a91046ea2 | -15.06798 | -44.97988 | 2025-09-26 03:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aec03f0b-d428-33a4-bd8e-568c467e7870 | -11.68291 | -44.45735 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79eb7020-84c5-3f7e-94ab-fde991d01a24 | -11.43177 | -44.93471 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce37a92d-7df5-3f52-9c5f-e3eaff11d88c | -13.85336 | -45.60769 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e8b64a2e-2254-3d15-bdd1-60c8e0d64232 | -12.87749 | -44.69998 | 2025-09-26 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1d8588e-0387-3e34-bc20-3179d5be2678 | -11.02172 | -44.35167 | 2025-09-26 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a928ac9-bf7c-3147-a6b0-2123b70a434a | -10.80736 | -44.43227 | 2025-09-26 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ddc5241-72d9-3802-a3e4-d04ad048a07d | -11.21239 | -45.6333 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b4096fd7-a824-3f09-8ca3-c3941d0e276a | -11.22829 | -45.62832 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b4cd231-cc16-3a9d-868d-fffd374e6327 | -10.00652 | -44.18372 | 2025-09-26 03:23:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e064202b-88cd-39df-8456-1121680bfd4c | -11.22691 | -45.56525 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ebc266cb-d530-3cd1-b2a8-a8f46b7d9344 | -14.82192 | -45.40419 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c800104-2d5f-320b-be11-b121daed4458 | -11.21395 | -45.626 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 154b479b-cbc2-3464-8be3-1464518d9344 | -11.22283 | -45.61913 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 536c5701-7361-3314-b735-9f42603da6c2 | -11.67974 | -44.45312 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 913f7aa6-6a4d-3cdf-ae20-e99e7bd2f70a | -11.42072 | -44.98809 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35aaafc5-c5c1-3419-9d39-056534d1a28c | -14.88127 | -45.54705 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f319aa08-157b-336c-b648-1b3400d89ccc | -14.81414 | -45.40819 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1db1eb2-394e-3c04-9023-61149d0f6cc4 | -11.21784 | -45.62809 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ddae8e50-6867-3278-ab51-9ef124722d5c | -11.23229 | -45.62987 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f7d1b687-7ee2-3c45-b8fe-b6370a8ef060 | -10.00111 | -44.17613 | 2025-09-26 03:23:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd391e27-77d2-34d7-b96b-cb7d5c5ea0b8 | -14.82071 | -45.40984 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a963ef49-b768-3ba8-ab37-cf6cdd61028d | -11.6779 | -44.42825 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4aaad47-9752-3e85-aa71-653a7f947b5d | -11.23409 | -45.62109 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e11b6e7-cdb0-35c8-ad5f-232d8641daa5 | -11.66315 | -44.45299 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89ec0d52-1868-3dcb-9796-87b77cf2a596 | -11.23545 | -45.55981 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| e7a21b9a-47e6-3654-b57a-f22f91d09d28 | -11.66728 | -44.46611 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8d683ee-9aee-32af-b090-ef722a193b68 | -10.57242 | -44.07674 | 2025-09-26 03:23:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcf27ecb-037c-31b2-a6cc-7d08681919d2 | -14.83349 | -45.38248 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2892cde8-dd94-3420-bf67-7b6c125e1c05 | -12.83984 | -44.71584 | 2025-09-26 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7bf020a-95b0-3417-bb70-ae57c0f00f78 | -15.06682 | -44.9852 | 2025-09-26 03:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d3d35c1-5468-38a3-ac47-ce26d10dfc2e | -11.21568 | -45.60265 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d591638-bce9-329e-a80d-abe0a4b22a77 | -11.47911 | -38.99849 | 2025-09-26 03:23:00 | NOAA-20 | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a001dcb4-3614-3381-bc97-e9a3e4c5eaa9 | -11.22793 | -45.59517 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f8ae7b3-c38f-3e60-8471-7ffa8a7f88fd | -11.42194 | -44.98222 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7f6bf06-1855-3e18-a332-b6e54de09aa0 | -11.38323 | -44.96153 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebaa441f-8941-3689-a7f5-f692536f2426 | -11.66438 | -44.44716 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1938fad3-5555-3b11-8e91-9003f0dc3084 | -10.00775 | -44.17766 | 2025-09-26 03:23:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75864f21-977a-3967-89b7-af2dcd671998 | -11.223 | -45.60303 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e2aa162-ad62-3a5a-8f42-49197691fd38 | -11.24284 | -45.61454 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2eaa21f-491d-3826-9cd1-0ccec5a7d79e | -11.23906 | -45.61251 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8bdf9a5-bc55-33fd-8253-4d8a16fe3f8a | -11.68329 | -44.43556 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2c3bab4-6add-31dc-890f-1dc24c2f8319 | -11.67132 | -44.42678 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca054e17-90b7-3453-a4e8-8bb5b0c89868 | -11.23599 | -45.57589 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b1a8283a-69b3-320f-a426-2d573184b421 | -12.8709 | -44.69868 | 2025-09-26 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fbe4409-7e62-36f6-b023-0c479c0111bc | -10.10981 | -45.31239 | 2025-09-26 03:23:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d185c33-8099-304e-8bed-473188bba09c | -11.21274 | -45.58117 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 54ca2199-e2e2-3198-8ae0-e2feebf06336 | -14.03532 | -45.5019 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9123f53-56fd-338f-9839-6cbf4d1244b3 | -11.00186 | -44.3473 | 2025-09-26 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f2a988d-b333-35a9-90c4-d118ceb9897f | -11.23871 | -45.59861 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b6e9240-f532-3ae9-b8c5-b0bb3a1b1d8b | -14.81757 | -45.41142 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc8d6470-3793-3451-a4f5-0f95288c74b2 | -11.2389 | -45.56179 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b9c1d2d9-fd5e-3c85-ae2f-519a90a434dd | -10.00519 | -44.17644 | 2025-09-26 03:23:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98718d65-277a-34b8-87f1-cae6bee7228f | -12.73542 | -43.45579 | 2025-09-26 03:23:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4641f36e-f7ce-31a7-9617-cf152383cb7e | -10.56465 | -44.08122 | 2025-09-26 03:23:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42b9bb31-030a-3148-9dbc-afcce4a15ae9 | -11.21074 | -45.62655 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f5217cd-02b1-3572-b6e3-7762bbf6282f | -10.11691 | -45.31387 | 2025-09-26 03:23:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95819a0b-c1fd-329e-9ebf-484f1d984367 | -11.66605 | -44.47196 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 240d3351-40f8-3f5d-81e4-a18a9485942b | -11.67435 | -44.44576 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 521d2df6-6aa2-3d14-b1cd-00c2080d2576 | -13.84521 | -45.61248 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc60ca37-dae6-34af-82bf-b50e0ca3ea6a | -11.66851 | -44.46027 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98a78fb0-5aea-306b-846e-f3128d122286 | -11.23744 | -45.56884 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fa8c9916-6e48-32b2-bc99-1142938d3d66 | -10.81163 | -44.4327 | 2025-09-26 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b4a3027-8b61-3004-aafd-d864092b4e37 | -11.2304 | -45.56719 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b688e0fe-2a13-3207-9a03-7dcda67c432b | -11.23746 | -45.62005 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 28ab3c31-cd09-308e-8e69-e6263bb51bcc | -14.03365 | -45.50111 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b231b426-188e-36a0-bfd7-badc7a5b57b3 | -11.43033 | -44.94168 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3aceaed9-e48b-3765-8d82-3e06f6722856 | -11.21494 | -45.6421 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fded5842-edb8-377f-88d9-4f3658111837 | -11.22638 | -45.60244 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc65a9a4-6d7e-345e-aa67-fb2bbb775d86 | -11.68243 | -44.42675 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 868b100f-8a4a-3478-93d9-f8b8d8fa18a7 | -11.23246 | -45.5739 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 99472c79-9c19-31a8-ad4e-96df85f4c370 | -11.20924 | -45.63383 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9ef9695-85c7-38eb-8136-d43da5013422 | -10.57123 | -44.08254 | 2025-09-26 03:23:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d95c8f7c-25e2-3707-be15-ed66086c5577 | -11.61507 | -44.4327 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 45a9aef5-82ad-309e-819f-7815d90b4ce9 | -11.0205 | -44.3577 | 2025-09-26 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f144d028-db47-3c3b-9576-821823d757a0 | -11.67877 | -44.44421 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e899a3d9-5405-3807-8835-37c42bf2edab | -14.03667 | -45.4958 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e04a6c2-4b5f-36d9-97af-8f8b5fc14a2f | -13.85061 | -45.62036 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b85ed1c-3949-3227-bb6b-435dd90710b6 | -13.85198 | -45.61407 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 45491a35-a187-322e-9519-7481a0de71ab | -15.3634 | -43.74643 | 2025-09-26 03:23:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a23177d-96e7-3b1d-bdae-1dab67364a0b | -11.23162 | -45.5971 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc526e7b-f03b-3dca-abba-9024b0130243 | -11.2406 | -45.60523 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 397c7cd3-5888-3c38-a30c-efc29376257f | -14.87469 | -45.54531 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 175ffdc2-d1db-306f-b234-c6d883a75f91 | -11.68 | -44.43838 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67674109-34e5-38c4-b4b7-7db2b0a2c5d1 | -11.68566 | -44.42389 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1f6b4c9-ff5d-3067-9bb5-e40a44b08a0a | -10.10701 | -45.30975 | 2025-09-26 03:23:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76ddc13f-9cbf-3980-85b6-0e253cd867a5 | -11.2245 | -45.59575 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56ee69a3-9d42-3d7e-8258-c3daf13e9104 | -11.2425 | -45.56141 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| eb3bba5c-2c90-3b7d-87ad-773330953d66 | -11.68169 | -44.46318 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d88ce974-1810-3c92-a1d0-97cbf16ae6d6 | -11.67755 | -44.45005 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 808e29c9-5236-3012-a849-b367685a6303 | -10.57376 | -44.08089 | 2025-09-26 03:23:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c86573b7-82c7-38db-96fc-a4bf8c2a9361 | -11.222 | -45.64386 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82637634-c092-3527-af00-1386d4b21281 | -10.80496 | -44.43118 | 2025-09-26 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c32c555c-cab0-3fe0-925a-ab658bc3cf48 | -12.84762 | -44.71155 | 2025-09-26 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdcd1253-93d2-3c52-8ad2-7a3b76e0f296 | -13.6833 | -44.29596 | 2025-09-26 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e408e10-f6bf-303a-b98d-ea013698a529 | -11.23395 | -45.56686 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 069e70e0-b8f2-3a3a-b2e9-3bf253b3ad42 | -11.0151 | -44.35019 | 2025-09-26 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0b8f851-8f90-3ba4-9f6e-c916d931372b | -11.23013 | -45.60434 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cd7159c-dd0c-3b3b-bd87-36d1f4b3ba08 | -11.66418 | -44.4619 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fda68ad-4ed4-33f1-b448-cfeb85dd259f | -11.22334 | -45.56559 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README7.md)
