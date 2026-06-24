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
| 79425071-5cbf-3e45-a933-a2af111b4310 | -8.6181 | -45.9854 | 2026-06-24 03:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 0109450b-b5af-3841-b663-d688583abe3b | -12.8349 | -44.3892 | 2026-06-24 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 77acb2ac-7a13-3bbf-8172-19e187cdce4a | -12.8548 | -44.3625 | 2026-06-24 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 356.8 |
| 3be88299-b79e-32d9-9f1b-79471826c748 | -12.8359 | -44.3422 | 2026-06-24 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 6c4fe808-106a-341d-a32a-097d5ef66f1a | -12.8543 | -44.386 | 2026-06-24 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 7c95bff5-1861-3cc3-94ca-d28780cef832 | -12.8552 | -44.3389 | 2026-06-24 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 685feab6-5739-30f1-a089-625bea343895 | -13.0635 | -53.3546 | 2026-06-24 03:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b70207d8-396e-338f-bf05-1cac5ea0fb43 | -9.37816 | -41.22108 | 2026-06-24 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3623984b-31d6-3de1-b735-c44c28f6d91c | -6.99486 | -42.89244 | 2026-06-24 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f1d3387f-7265-3111-bd76-b958e01a294a | -11.30725 | -43.33372 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2c50ee51-9873-3a8e-b65b-57b971756921 | -11.29304 | -43.3261 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8a0bdc70-277e-340d-b086-63f7e75eb12c | -11.23951 | -43.3471 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 043e559f-f586-39e3-9bd5-cc5743330f3d | -11.30637 | -43.32961 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 915e29a4-5d86-355f-875d-6b22a94df611 | -6.99818 | -42.89438 | 2026-06-24 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| dcb309e0-20df-3380-b83e-4f969c197b2e | -11.24376 | -43.36066 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 35360088-015d-31ea-9a6b-b3270d5e3f84 | -11.24084 | -43.34065 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 721d36a4-5333-35f7-867b-694c16df071f | -11.237 | -43.35927 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 5e920be1-13c6-365e-98fd-2fe117f95cdb | -11.30386 | -43.34206 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e19d876-7ca5-3938-9451-8146332b4e84 | -11.30596 | -43.33994 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb76736d-79df-3640-bd60-ed0353920b1f | -11.2665 | -43.35278 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3e607e95-1b38-3ae7-b464-d184a939526d | -11.30186 | -43.32589 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2ca39657-479a-34af-aac8-d906a2b44eb3 | -11.25052 | -43.36206 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a4bc0e60-118d-3186-89c8-b5912a53e041 | -11.25575 | -43.33659 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 51d6f5d6-074d-3783-aed4-9f3d2582ed6d | -11.2984 | -43.33427 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ad570406-80f6-34bb-8101-1f955d96b2cd | -9.37722 | -41.22589 | 2026-06-24 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9077812e-8108-3f31-8ae9-b64b9452176e | -11.24246 | -43.36699 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 82e29cce-d886-3354-9036-047f6d3ba4e8 | -11.26175 | -43.3493 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12161722-7e4f-39c2-9ab2-00ccd19dd7cd | -9.37833 | -41.22645 | 2026-06-24 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba0856c8-c342-3e44-bde5-2d9fc60ebfce | -11.30856 | -43.32746 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 096d5224-3826-32a2-a37d-0c26d40da5b8 | -6.9969 | -42.90116 | 2026-06-24 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5c723c5c-ecee-3de0-9fbe-67bd045e6e0f | -11.2685 | -43.35069 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8fd538e-32e1-3a91-ad80-ea9412db869b | -11.23572 | -43.36549 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 18042578-1ad2-3894-90ba-4b4d8a55bf16 | -6.99354 | -42.8992 | 2026-06-24 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 85a5e9da-141b-396f-81be-1a0fde2db6f0 | -11.23823 | -43.35331 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 35258ea7-acae-3726-bfa7-fa69539003d5 | -11.2672 | -43.35685 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a73184f-e35b-3e1c-acf5-a946084e90d9 | -11.26526 | -43.35888 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19fc2369-4b58-33e6-a19a-787900068a2c | -6.98989 | -42.89957 | 2026-06-24 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dfb3619f-3b3f-3323-8869-8c41f4dedd9f | -11.23277 | -43.34562 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 894bca7c-23cb-39c8-a803-34517527606a | -11.28588 | -43.33504 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 037e5062-47a8-3585-baa6-ce38fe362606 | -11.25726 | -43.36356 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2642c58c-4f10-37aa-876c-ee9307200631 | -11.29386 | -43.33054 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 32da3ba1-5738-3c32-bd62-81b97a8d9568 | -11.26399 | -43.36509 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37e4edaf-e45c-33a9-8866-1c534d3149b5 | -11.25916 | -43.36154 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6a86e9b7-31b9-3592-909f-35153233b002 | -9.37924 | -41.22161 | 2026-06-24 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 489032c4-c5d4-31d7-8a38-7b596564b042 | -11.30511 | -43.33587 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ddc7567b-92e5-3d74-9693-a8f58d1752cc | -11.2952 | -43.32412 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 025ff254-9b07-333f-982f-5918435280a4 | -7.37685 | -42.80339 | 2026-06-24 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1d657f68-96aa-35ce-a69c-4f6a5c719a0d | -11.24758 | -43.34209 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 095b8f27-05b5-3f84-8437-ecf6313a797b | -11.29968 | -43.32798 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2fad20d2-a393-39fd-b670-1741312257a9 | -11.30054 | -43.3322 | 2026-06-24 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b6939a45-3c2a-387b-a4d1-da884ae9fcc2 | -13.0635 | -53.3546 | 2026-06-24 03:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 82e368ab-ef4e-39ad-9b65-d6bad08b9eed | -12.8548 | -44.3625 | 2026-06-24 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 323.7 |
| 8bf1362e-897d-309d-a704-15e380438ae6 | -12.8359 | -44.3422 | 2026-06-24 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 235.7 |
| f447bff4-18c4-39c4-84c6-846a64dcd156 | -12.8349 | -44.3892 | 2026-06-24 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7cbea7a2-be5f-3790-82a6-a8b3b7422535 | -12.8552 | -44.3389 | 2026-06-24 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 838346bb-fb9b-399d-b839-833bc7bccdc7 | -12.8543 | -44.386 | 2026-06-24 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2baec31e-c609-34ac-a3ee-339839da9a80 | -12.8354 | -44.3657 | 2026-06-24 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 509.9 |
| 966bd2e4-299d-3141-a1db-9487d48887d6 | -12.83739 | -44.35931 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| cb3c0031-fb30-3a19-bc8a-71a3ddcf53c1 | -12.78353 | -44.43934 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5fb2e818-9eaa-375a-a944-4e50d71654a6 | -12.77749 | -44.4449 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aa83149e-ac91-30bb-bef0-fbdfa581ea2d | -12.77658 | -44.43765 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2c23b8d-faa7-3b08-8f4d-86ebcfb4b843 | -15.72764 | -41.35355 | 2026-06-24 03:30:00 | NPP-375D | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dce80d0f-55ce-352a-b9c8-6fba39227039 | -12.77909 | -44.45966 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3ea5f359-cd33-30d3-bfbc-b191222b32c1 | -12.783 | -44.45343 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9a16a104-5c10-3d59-b894-bc7259b69ab1 | -12.86846 | -44.37231 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f315d2f7-5ba2-38dc-a4a4-983614eef69e | -13.18214 | -43.40759 | 2026-06-24 03:30:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3669e461-606b-30f0-af3a-601d6d823976 | -12.77893 | -44.43811 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a66df544-7b0b-3c7e-be37-bed29a6d4c01 | -13.18335 | -43.40184 | 2026-06-24 03:30:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6f767b29-275c-37af-bb61-7b528352cdf9 | -12.83992 | -44.38137 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| b4b33bdd-a54e-3d95-843c-3fbe5ec5983b | -12.77604 | -44.45176 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 92b41ce2-7e46-3250-b39e-7a4bdfce6ed7 | -12.78444 | -44.44664 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e2d15bc-1bfa-3abc-bf81-25f0f3c8f44b | -12.81355 | -43.90426 | 2026-06-24 03:30:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38a2e247-70f7-3ad2-a228-b8677d07a463 | -12.78754 | -44.45455 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1ef51082-ee20-3dd1-a373-46f9233e5624 | -12.84287 | -44.36765 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7e7f9028-925d-3d52-b091-704950d1e7b7 | -12.7736 | -44.45126 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 977633b1-38be-3049-a2f3-a0e594826cd6 | -12.7751 | -44.44444 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69e06405-8fef-36dd-bd21-a295b95c7190 | -12.81486 | -43.89814 | 2026-06-24 03:30:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 168aa3e4-cc92-3c1f-916a-ef31a2a8da8e | -15.75933 | -43.23507 | 2026-06-24 03:30:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5ec8b804-bbae-35ca-907d-54d04bd3c80e | -12.84981 | -44.36921 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 56103f5e-c6a9-39ae-bd6f-a500fc63f04a | -12.84579 | -44.3541 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e33458ec-8261-38e8-9483-8b359ced9b3d | -12.78207 | -44.44605 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7e3d73e2-c0a0-3d70-b511-1109d595ad14 | -12.78059 | -44.45282 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b755d294-6fe3-3582-b0fb-8dee6dd1f750 | -12.84434 | -44.36085 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4fc1380f-0426-3d7b-bdf5-e696c44c3798 | -15.01805 | -42.37315 | 2026-06-24 03:30:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d5b93c1-6c8a-37af-a933-f90fe4e7e20f | -12.83042 | -44.35789 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 53bc19e7-236c-3451-b8ff-3bd4482f64f0 | -15.75311 | -43.2338 | 2026-06-24 03:30:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c2879414-ad92-3fc7-8f86-bc3ac0e893b5 | -15.01206 | -42.37193 | 2026-06-24 03:30:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1aacb95b-be2a-3a08-8d4e-978550f9cf32 | -15.76035 | -43.23042 | 2026-06-24 03:30:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 128f4b55-600f-385d-86c7-ff935e267564 | -15.7268 | -41.35762 | 2026-06-24 03:30:00 | NPP-375D | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8fcd9370-c51d-3286-b115-525274911b53 | -12.84139 | -44.37453 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| be4e7089-f32c-3362-b6b3-3f3aff283a45 | -13.18177 | -43.39945 | 2026-06-24 03:30:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 71107a66-44eb-3060-b2bb-19b202357753 | -12.78587 | -44.4399 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 070a20a2-791f-3296-8bb3-b3096913cf33 | -12.87536 | -44.37404 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3f7787d-71e1-3aa1-bc1c-076c02b96582 | -12.83444 | -44.37296 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a41bcc66-fc0f-3cbc-b3c3-59e24f1c61a9 | -12.83299 | -44.37969 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| dbfb403a-86f5-3ad9-9164-ca191cb872ba | -12.84835 | -44.37604 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5acfab3b-8554-3bbc-a9d0-b43d67802d55 | -12.82752 | -44.37131 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 26438203-16af-38d7-9e3e-2f6326859a36 | -12.85127 | -44.36244 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a66de583-d216-3f4c-b602-ee43d559d51d | -13.18052 | -43.40519 | 2026-06-24 03:30:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9e550e56-2ee1-35fb-9ecd-1a615997b5d6 | -12.82896 | -44.36465 | 2026-06-24 03:30:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |


[Clique aqui para ver as próximas entradas](README7.md)
