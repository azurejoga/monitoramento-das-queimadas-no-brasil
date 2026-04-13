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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 873cc13a-f18e-3158-a7e8-3446c363b0dd | 1.0926 | -60.53141 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54d6cf42-8aee-3ee5-b6e4-14c9ff529575 | 1.10791 | -60.51783 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d04ba304-d6fc-3d1e-9c17-e8cf99305b83 | 2.17189 | -60.703 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54fad271-5613-3876-952b-b60dd94a44c2 | 1.57091 | -60.33905 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 488fceeb-78d6-3dab-bacb-a77492252040 | 2.19951 | -60.81146 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79d22433-74ae-395e-a7bf-ef9a31d8ff8f | 1.10054 | -60.53767 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a901341-48eb-324e-876d-8ab9bb888cd4 | 1.0994 | -60.53036 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca4cec07-f435-3660-a9ce-f9fe8d28ebfc | 2.38794 | -60.96852 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe76e768-ddb7-303f-b3ae-dee72c88c226 | 3.31311 | -61.23571 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 275e85cd-0fd4-333c-abd1-e50d96e14856 | 1.09713 | -60.5382 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5891227-b87b-36c9-8b66-539f67c9c734 | 3.88258 | -61.84558 | 2026-04-13 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92659332-b347-3331-b5f4-2862d13fbf2e | 2.38324 | -60.96129 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aa478c5-acd0-377a-99fd-2cccbaa7b987 | 3.23278 | -61.20612 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83d35cbe-c0de-3d43-8111-ed485b69e3b9 | 3.23571 | -61.20152 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f04b7cde-2799-3b75-851c-9bdff3c68373 | 2.37684 | -60.96623 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a84c000e-c586-3e0e-abb3-8578b745c35f | 3.33458 | -61.23256 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f246e934-c563-3075-9f5b-6ab292e99463 | 1.10394 | -60.53715 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c436ce2b-ae42-3f55-bb23-b3562956e5c4 | 2.78214 | -60.2029 | 2026-04-13 05:23:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 580c143e-505f-3275-9a91-961436aa1897 | 1.11358 | -60.53193 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 143acdd1-a321-334f-9e89-4a45d41df69c | 3.2729 | -61.1878 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 485f0260-891f-3592-bc7f-cc2df7b7649b | 2.17248 | -60.70678 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa794dde-6d42-3a28-8ddb-9e5cdfda6040 | 2.08546 | -60.532 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 294a97c2-2c21-37b1-a232-21d77c9e6698 | 1.11245 | -60.52462 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01a56c03-34d0-3c35-848d-2897044bf2b6 | 1.10564 | -60.52565 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9c9b703-8be5-3f8f-9e93-969a1992a2d0 | 2.32519 | -60.94173 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51f4223f-4add-3be5-bde5-35274a81196c | 3.31731 | -61.23927 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7f9d5e3-07c7-3dc2-a626-be1653ccf2f0 | 1.10337 | -60.53349 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7993c72-e86d-3968-9fb1-1432e31eb62d | 2.19891 | -60.80764 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eddc49b2-8a3f-364a-87a2-819a82b2b135 | 1.26881 | -60.31844 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3352e0b5-60a3-3ac6-926e-f6e3d574e8d7 | 1.10734 | -60.53663 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a56623b-9c2a-3370-a404-e103fee0b711 | 3.31668 | -61.23515 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8199bbc-d71b-3e00-9864-a7122be2f61a | 1.11415 | -60.53559 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10c021e7-a2ef-3fd2-bb5e-1e43a6053f4e | 1.11301 | -60.52827 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0c08845-f341-31e6-934f-21b6b1f3fcfc | 3.30891 | -61.2322 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9715bd6d-09ff-3eb7-9793-63fe3c31f753 | 1.11018 | -60.53245 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dacfaac-c108-39ec-a392-bc177a35ec2b | 3.87748 | -61.83719 | 2026-04-13 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f5846d2-671e-34b7-9e32-e00979e204b7 | 2.38384 | -60.96517 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac3b302b-9f33-33ee-b514-267b45ebec4b | 2.37275 | -60.96288 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dc4f5f7-f49e-3dbc-8bf3-aae7bf52dfb6 | 2.0883 | -60.52768 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0f9ee61-ec7d-32c3-9a51-7b33e897b530 | 1.10791 | -60.54029 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 371b5446-8cad-3043-87b2-1f6c64d10e33 | 1.10451 | -60.51834 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd2bec76-280d-369a-861b-87f5de59acaf | 4.30824 | -59.72767 | 2026-04-13 05:23:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9c34048-1413-32c9-9023-aec10efeb6cf | 1.83755 | -60.74181 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c366def6-5950-3375-ad39-714240fe788b | 1.10848 | -60.52148 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bd34315-77a0-39bd-bdc2-406c72f7cd27 | 1.65218 | -60.14162 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54dcf3b1-8fc8-364f-a416-56b22347758d | 3.93969 | -59.7024 | 2026-04-13 05:23:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0484542-2d25-340b-8329-e8af21af2364 | 1.1011 | -60.54134 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d96377a-3fcc-31cc-b4fc-67edb49c024b | 2.37625 | -60.96235 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6e8a572-50a2-35b4-8d83-086764d58a35 | 2.576 | -60.54949 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ddaee5f7-eb0c-3b54-b574-382dd2db5d39 | 3.33037 | -61.22897 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65bde20c-867b-3086-80cc-d928ac213a55 | 1.10678 | -60.53297 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75a5df16-96af-34e9-9c17-1c519a8ce493 | 4.31163 | -59.72711 | 2026-04-13 05:23:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cfabbf5-4ddc-3b83-8c6c-fc8c50d86ef8 | 3.32678 | -61.22947 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4e1fe01-0ede-3372-9d92-5af9c2b29305 | 2.38734 | -60.96464 | 2026-04-13 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b88dd58-e15d-3202-b1b5-2245b991ed4a | 2.02614 | -61.0931 | 2026-04-13 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfd7fd83-bd53-3693-9da7-15e7621da265 | 1.09544 | -60.52723 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a05bcd1-baef-3b8f-ad33-38a654912ba9 | 1.10167 | -60.52252 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f93c73b-9a5d-3493-a2da-5821676c9267 | 2.08488 | -60.52822 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c4ca2a5-69e8-332e-99b9-f4e3ac0abec5 | 2.57256 | -60.55001 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd0a1335-9d51-3e60-922d-02932ef85050 | 1.71092 | -60.47135 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 831ee38f-7784-3963-b829-58e098ecb464 | 2.07859 | -60.533 | 2026-04-13 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bfa8df5-cea3-3c3e-a991-398436b1cb52 | 3.32089 | -61.23871 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beb6e682-141d-3943-8feb-3149698e774f | 1.09884 | -60.5267 | 2026-04-13 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eb10933-daab-3ceb-bf7d-35adf4c63ede | 3.31605 | -61.23107 | 2026-04-13 05:23:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01c50229-6b9b-3b01-81b2-cddfe0c24989 | 1.09829 | -60.51772 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aed1ae9e-d2f7-32ff-8283-6a69f244feb8 | 1.10637 | -60.54251 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 025bc1ab-b5c1-3922-9cfa-696b43149606 | 1.10952 | -60.53681 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cefcd57-afe5-39c7-8eba-f365ce230ebb | 1.10158 | -60.53806 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8b6ff8a-72d7-32ad-bf8b-0ef7d70e0f12 | 1.10473 | -60.53237 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 825cf680-1662-37ca-b404-f0779daf975e | 1.10788 | -60.52666 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76acdb28-844d-3221-acdf-4f5683a3eb87 | 1.09994 | -60.52791 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 376895c6-6168-32f4-b585-bb64c2b2c104 | 1.10076 | -60.53299 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 196ac1bc-834a-30ba-ac8f-7f60c5ddb4e3 | 1.11664 | -60.53047 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d829142-fe1c-3d09-a6e5-9a8dbe222312 | 1.1024 | -60.54314 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4143558b-e0fc-3f66-822f-1a22a766e0fe | 1.11267 | -60.53112 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1077f1ff-df9c-3b08-8b79-675fbbbf8838 | 1.11582 | -60.52537 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f379bef6-811b-3b93-88ee-801df3d43255 | 1.10227 | -60.51711 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2e69a37-4264-3a02-a67a-734414ba9473 | 1.10391 | -60.52729 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1840328e-f12b-3efe-91c3-e65ee88788f7 | 1.11348 | -60.53617 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0551ef68-4e6b-3dfd-85bb-b89c604f2263 | 1.10309 | -60.52221 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6585a4b0-cd2d-3e25-9275-52f5838d270f | 1.10624 | -60.51647 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcf7fc5b-d8d4-37be-871b-a40b78f6e3f6 | 1.10706 | -60.52157 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f011b14-24a3-3f43-a34d-af07e9ad9b59 | 1.11185 | -60.52602 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 702fc94a-74f6-3e73-8e69-dc00f1752e51 | 1.09912 | -60.52282 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5d6f2fa-b5e2-3cf5-a677-b46b9d62c73c | 1.1143 | -60.54124 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc6f6c00-4184-3e0e-9601-e6c075edb6ef | 1.10555 | -60.53744 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a69a59e-6ad9-35a3-9dc4-5b5800ed1a8a | 1.1087 | -60.53174 | 2026-04-13 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73341dc6-f8fe-3b12-b81d-337485ce7804 | 2.37517 | -60.19314 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41e3c752-3b1d-343e-b1ea-5bce8cc384c9 | 2.57187 | -60.54675 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b00702a4-17d7-3320-a9e3-56e9a0a494b6 | 3.33394 | -61.23274 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5722b44-bb80-3166-a25d-ded03259a8ce | 2.5202 | -61.67439 | 2026-04-13 05:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c770c15d-ff2a-334e-a3dd-8efa208fc51f | 3.23454 | -61.20409 | 2026-04-13 05:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 644c8522-9095-3b51-a007-56481cefe9b2 | 2.38725 | -60.96422 | 2026-04-13 05:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80491a3e-7f40-3bb9-8904-19a047b038d6 | 2.08854 | -60.52767 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c1357a4-3c3b-3931-b760-cbad5f2e13f5 | 2.53664 | -60.35089 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4c7382d-67be-323e-bc67-3008678a5676 | 3.25725 | -60.20105 | 2026-04-13 05:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c44394b-da77-3438-ab8a-a719e7ca72f5 | 3.87846 | -61.83961 | 2026-04-13 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8dd1ee2f-02c0-3417-8f7d-0f358352dc12 | 2.08073 | -60.529 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df7ddb09-c760-3ed5-ba02-f30bf4e621b9 | 2.02181 | -61.09329 | 2026-04-13 05:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10022006-50c5-324b-8b03-e31170a719dd | 2.08464 | -60.52837 | 2026-04-13 05:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
