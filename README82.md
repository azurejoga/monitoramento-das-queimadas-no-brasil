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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d788f79-0bbf-3a45-85eb-b77955812da9 | -17.69862 | -41.84553 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| 748f078c-1411-3926-9894-a26c54933f51 | -17.54022 | -40.95275 | 2026-09-14 15:44:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| e4e64e08-4244-3dea-9a11-95b821e5a5ed | -17.69818 | -41.84084 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| e70a55cb-164e-34dc-b5b4-d0cefd4a95a3 | -10.77022 | -46.30353 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12f6a25f-cfd5-3895-88ba-1b60cc3c0597 | -15.99707 | -40.68125 | 2026-09-14 15:46:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e7af2133-c0eb-3a2f-89c5-e0e081503f71 | -16.05362 | -40.48425 | 2026-09-14 15:46:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 86689be0-1456-3995-9854-a08e63cafac6 | -13.40664 | -41.61087 | 2026-09-14 15:46:00 | NOAA-20 | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f2584685-c67c-3f27-8160-bd6cc6baa267 | -14.23088 | -41.14477 | 2026-09-14 15:46:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 4a165029-93c5-3454-80eb-9a122a6840e1 | -11.63391 | -40.35984 | 2026-09-14 15:46:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6675e274-dd3e-35fd-a2d4-372160d3b952 | -14.651 | -42.02526 | 2026-09-14 15:46:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 953ce1c2-32e8-3aab-81be-bf98b8b14f68 | -11.23305 | -43.44875 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 056c2cd3-b3f0-3b4a-9ea2-688b19e182a3 | -14.34584 | -41.45943 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 6e5de810-362f-3a09-847b-3124feb4a7c5 | -10.32493 | -45.29097 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 82e23ef8-6a2c-32c8-8fcb-51adfe5f2431 | -10.476 | -40.87441 | 2026-09-14 15:46:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f93671bd-5592-30d1-9638-19f2f8917b66 | -10.79305 | -46.24827 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ffb41bee-12a9-3f4a-99b0-0ae70b84fe2c | -10.3067 | -45.33309 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| f61485b3-da19-3aba-92ba-ffbe5e1d1c81 | -13.27917 | -40.32775 | 2026-09-14 15:46:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| d921e512-3544-3931-877b-4e4efccdd7b6 | -11.23805 | -41.03521 | 2026-09-14 15:46:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 98f2e51e-eb66-37ce-b60b-a2314dc9ded6 | -15.19263 | -42.129 | 2026-09-14 15:46:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 415e7be7-8e02-30c6-8085-910bbc1d42ad | -14.57379 | -40.71629 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d7fe3572-e479-32b9-b1ae-993db1ec13f5 | -12.42627 | -39.2837 | 2026-09-14 15:46:00 | NOAA-20 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4a0ad6c1-a5b1-30ed-9fc4-3ed601ab76e5 | -10.43637 | -42.7397 | 2026-09-14 15:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e0ba35f8-ae84-34c0-a690-8accddb8ef5d | -10.5247 | -46.307 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 651adf72-3979-3e05-8904-339886cf88ed | -13.56751 | -40.62965 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 439a1255-25f6-3696-b211-e32c42a3dc0a | -17.26213 | -41.51776 | 2026-09-14 15:46:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 4055680b-de2d-3400-9e97-62b69a5a3ecc | -11.2142 | -43.44629 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a438214d-ed66-3441-93e1-962a82789d44 | -10.32642 | -45.30372 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a346b235-494c-33ed-91b6-6fc6f83bb09a | -12.74176 | -40.42559 | 2026-09-14 15:46:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88d1dfb1-2b97-3487-9722-2793055925be | -15.17153 | -43.84798 | 2026-09-14 15:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5c90d31d-6df3-3555-afef-fd511258e96c | -12.71769 | -38.98888 | 2026-09-14 15:46:00 | NOAA-20 | MARAGOGIPE | BAHIA | Brasil | 2920601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 3ae4fc29-168e-3124-a5a2-667f7f34e143 | -12.06967 | -41.7149 | 2026-09-14 15:46:00 | NOAA-20 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d0c93a83-33f3-343e-825d-92b98eec1abc | -12.12374 | -44.20812 | 2026-09-14 15:46:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 89bd0274-ec0d-3f7b-9b42-2d3eb08e4e4c | -13.21696 | -39.81433 | 2026-09-14 15:46:00 | NOAA-20 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 496378c8-05b8-32c2-ac65-c369db049e82 | -15.1716 | -43.84261 | 2026-09-14 15:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bd2bd0aa-d629-3b4f-8ed7-7a556b487542 | -11.50732 | -45.76023 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c98ddb99-8b1d-3460-a717-d82a61ce1d3b | -11.94328 | -38.41817 | 2026-09-14 15:46:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 46ad9da0-db66-363e-a1b9-1c71dfe5f9a2 | -14.34624 | -41.46298 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 2f986dfe-f196-32dd-9b58-ef4dc7af0ae6 | -11.22695 | -43.4495 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4ff451e4-83d3-3567-bbe0-05f3db69a1ef | -11.29375 | -41.60885 | 2026-09-14 15:46:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b66ebf9d-0653-3f14-9194-994a1c3b2930 | -10.80196 | -46.26256 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e2ae3a51-8eaa-3f24-b4a4-6cf4167759f3 | -15.17098 | -43.8423 | 2026-09-14 15:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 14da5d92-c26a-39b1-824f-55d86a2431b0 | -14.39043 | -39.3386 | 2026-09-14 15:46:00 | NOAA-20 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 6404157d-2be5-3793-ab32-f7009c3222aa | -14.37695 | -45.24795 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| f134d8ad-8a1e-37fa-a6f4-70e552ac7ebb | -11.23901 | -43.45087 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 66f06817-190d-3c3b-87d5-22128d20ccc6 | -11.37725 | -43.95052 | 2026-09-14 15:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f5c77107-1a67-32c4-97af-6000eae39db1 | -11.52772 | -45.77107 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 7fa28425-a660-3bd8-bef5-d11d62538d6a | -11.22451 | -43.43365 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d519344c-9dbf-3354-8db5-a4fd4ce6e62f | -14.25465 | -40.40395 | 2026-09-14 15:46:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 695a0823-9d68-3e8b-8a62-fab9dd53b803 | -11.3745 | -43.95716 | 2026-09-14 15:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 21ee63e2-aa43-3253-bc59-209c370c5f38 | -11.5129 | -45.7659 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1c19c099-df24-306c-b519-c26ec249c9cb | -13.90109 | -41.29033 | 2026-09-14 15:46:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 982a9994-438e-3520-91d5-c84f3c3625a5 | -11.50512 | -45.75988 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 68df5573-89e6-3aab-b8a9-c7faf0d6077a | -15.19098 | -42.12699 | 2026-09-14 15:46:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 4c964d19-e270-3dad-9d4c-63cf0d92f503 | -13.59681 | -40.65255 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8ed6516c-0cae-3faa-a606-56bda6fafc87 | -15.09484 | -41.26644 | 2026-09-14 15:46:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a929bf0b-8bc2-3cef-8d26-8186a6b89627 | -10.30279 | -45.3365 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 2865859a-0f82-3f8e-a3fa-795ec7709475 | -11.18326 | -42.8181 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 2e34f5a2-707d-3d46-8197-bb3829da9c10 | -14.8144 | -40.81416 | 2026-09-14 15:46:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 397520d5-9ade-36c6-adeb-fbce14cb2bab | -14.57074 | -39.91188 | 2026-09-14 15:46:00 | NOAA-20 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7afd17e8-7fce-3713-9668-0540cf3fd06d | -15.19215 | -42.12465 | 2026-09-14 15:46:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| bf076bd7-569d-3f90-8a2c-5d282ca22eee | -12.37646 | -40.56916 | 2026-09-14 15:46:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c144e0d-6c1a-3fb7-a4e9-bbcb05d2f892 | -17.59363 | -44.61103 | 2026-09-14 15:46:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0944456-2d2c-3f18-b105-552695b37e22 | -10.30608 | -45.30554 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a97245d5-a7fb-3a5a-b5b7-9f1966792d39 | -16.06102 | -40.64783 | 2026-09-14 15:46:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 6edb2c3f-bbc1-34fb-a0b9-c269c7d1d402 | -13.55811 | -42.41666 | 2026-09-14 15:46:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5a10938d-9610-32f6-a35a-5db8b68ed2de | -14.38001 | -45.25475 | 2026-09-14 15:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 3f48b722-05ed-32f8-a4af-02f3ac573625 | -12.20472 | -42.23241 | 2026-09-14 15:46:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 1c09e4b6-2680-3172-89c5-02276f844f2a | -10.77741 | -46.30269 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 27e9a532-88c1-3746-a269-847754e760ea | -15.63373 | -40.67906 | 2026-09-14 15:46:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b5341d76-e94e-3668-b2af-50b056b47fd5 | -14.4671 | -41.34562 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 39eb035d-bb89-341c-bba1-1b1d01bf0e80 | -12.12311 | -44.2026 | 2026-09-14 15:46:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4bd20e32-d6c0-33e4-ae18-f979d9680303 | -10.29986 | -45.3333 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 9475d9ea-a6ee-3a8f-ba93-cd80206b2e9b | -10.78128 | -46.24417 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3f661347-815f-3b48-9546-710c8f24f93d | -16.06063 | -40.64429 | 2026-09-14 15:46:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| af8bb74f-25cf-35c9-91c8-b581365a64b4 | -14.36983 | -41.38263 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ce80a066-fdff-36b5-96fe-554fddc642f7 | -10.64182 | -46.09398 | 2026-09-14 15:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7db18187-fa7f-3cd9-8686-a82c59689781 | -13.57278 | -40.62923 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| b018be03-ebdb-3413-96de-5d190f223b43 | -14.23172 | -41.14183 | 2026-09-14 15:46:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c5db8c8c-c63b-3e7f-b786-eedf7fefecf1 | -14.55219 | -40.66954 | 2026-09-14 15:46:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f2849dc-4349-3cbf-a8f9-c1ec29aa01c6 | -12.47129 | -38.34626 | 2026-09-14 15:46:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 75589a2f-0c7e-337e-836d-34f00e232f39 | -12.1784 | -43.54647 | 2026-09-14 15:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 84ee2b3b-481f-32db-8770-43d1c71b52d5 | -11.17488 | -42.79768 | 2026-09-14 15:46:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3ac6e10a-4caa-3b29-a347-f8ef126027a2 | -11.2983 | -41.60126 | 2026-09-14 15:46:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c1e162e3-4d49-3d70-8a9f-5c03d9c29c52 | -13.59721 | -40.65599 | 2026-09-14 15:46:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5c732bb5-76b4-39c8-b532-ffddb6496160 | -10.81223 | -46.26147 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 0c94eb95-7202-3b16-bacf-b29e7b2c1efd | -16.12001 | -41.34278 | 2026-09-14 15:46:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7f1049c2-dd32-3ef5-bd26-03359de4099f | -10.78591 | -46.24946 | 2026-09-14 15:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a8e03d3c-9f6c-36ab-a6e0-456be0f66991 | -12.47643 | -41.4232 | 2026-09-14 15:46:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 184861f7-eb4e-3847-b5cf-214c9475a1e0 | -11.50029 | -45.76106 | 2026-09-14 15:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90774fe6-9d5f-3ccb-bd55-3fb118f2d721 | -10.32348 | -45.2785 | 2026-09-14 15:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| bcbe1b76-5831-379d-9113-ff58dcb267b0 | -14.57341 | -40.75983 | 2026-09-14 15:46:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4f31c74d-7765-3436-8850-fe678c88b9ac | -11.18147 | -40.52683 | 2026-09-14 15:46:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 4b60e8b4-d01a-3fac-8aed-afcef7697d4a | -11.23843 | -43.44618 | 2026-09-14 15:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1e0a3c2f-77ed-3fc3-8105-e74614cc04e8 | -16.14887 | -43.63203 | 2026-09-14 15:46:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 159b9e8c-db96-34da-8e89-c6b5808e0d5a | -14.48222 | -41.37868 | 2026-09-14 15:46:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2139e707-6f4b-3b68-97bb-03d670bc8a45 | -11.37152 | -43.95642 | 2026-09-14 15:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 38e76b3b-061d-3e9f-ae24-503b45010a30 | -12.12984 | -44.19975 | 2026-09-14 15:46:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8157cfd5-aa3b-31ce-b776-493dcc81e3ec | -14.3066 | -40.81074 | 2026-09-14 15:46:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5a0f4769-9eff-3747-8dd1-34e7f3f8126f | -14.75415 | -41.84356 | 2026-09-14 15:46:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0074c79c-50bd-3e9a-9f36-c00e4cc1da15 | -15.46329 | -41.7535 | 2026-09-14 15:46:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README83.md)
