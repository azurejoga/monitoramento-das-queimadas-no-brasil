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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 098152a8-34c7-39ae-8ebb-b80259bc2f85 | -6.95489 | -45.25928 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e30b2f6-37c8-36e0-94b1-d86c23a6e1a0 | -8.72553 | -45.17008 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9e243cb7-dccd-3e87-b2a2-a878da205728 | -5.97247 | -40.91281 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cfcf2ad9-1800-37a5-910d-e66838c9d8bd | -6.94945 | -45.28857 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4288307-be80-3502-b257-686be57d1ccc | -7.23032 | -44.27193 | 2026-10-08 03:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecd6e064-73bc-3801-afdf-a360800d3ca0 | -5.72677 | -41.76588 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3275015c-f18b-3111-acfa-fe3101dd2527 | -5.73373 | -41.75945 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 918780cd-5fc4-3f79-a81c-63469d544275 | -6.16026 | -39.43932 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| bc8c7f2f-d3ec-365a-9779-dff328fe8756 | -7.47727 | -42.85534 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 05ca16d0-d62d-3f87-a79d-19096ff30387 | -6.92747 | -43.66661 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 78081928-8ac3-36c3-9dcf-1d5b15619307 | -5.75083 | -42.06575 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 530c4975-e7fe-3823-b3cb-fa48dfc60707 | -8.72979 | -45.18361 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 780ac925-a7e6-3abe-a2d6-a70007111e37 | -8.74102 | -45.16121 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3be40a7a-23f2-37e0-b10c-953a331b3086 | -7.10732 | -42.53347 | 2026-10-08 03:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94fdea3f-0296-3007-9ffb-97af8483e43e | -5.73174 | -41.77076 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d6ed72dd-d93d-3c38-8d5d-871923dd7205 | -10.24423 | -36.33668 | 2026-10-08 03:42:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 986a0fe4-63fc-3651-b764-d2e39d976592 | -8.72439 | -45.17594 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 724a5ec5-1daf-30fd-934e-ebdce14a40d4 | -5.74005 | -41.75666 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ff80ee9-6859-3457-ae62-a9d463e8073b | -10.24571 | -36.32789 | 2026-10-08 03:42:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 5df2793f-9163-3d64-8e98-b7bf90d880a8 | -4.35426 | -43.79241 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 12acf9c9-8d62-3995-96f6-3ca885765d28 | -8.72784 | -45.15821 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bbe803f7-7ca7-386f-bb12-a220e5846bd2 | -6.83518 | -39.56126 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8d6ca1b6-89e4-3b08-976e-709d2fd299d1 | -7.20669 | -45.35211 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77cb0157-3a00-3465-a645-13fe4903e143 | -4.34776 | -43.79096 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0c62c8df-d4e0-370c-b5b3-8978329d6e22 | -6.59822 | -37.89669 | 2026-10-08 03:42:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d1372f8d-e441-3f4e-a55c-ca3ce2dc9eb6 | -5.77098 | -42.05278 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae87349e-e50e-36fe-9029-348074b0b84e | -8.21433 | -46.37772 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5e43273e-7677-3be5-a185-ff85b1c360e5 | -5.7261 | -41.7697 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7f553045-01b0-3c00-a73f-9601d0ceecf4 | -4.35323 | -43.79815 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 11fc23c6-4791-3832-a50a-d82935b06751 | -6.90236 | -40.91085 | 2026-10-08 03:42:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2457156e-9b1a-3752-a739-c70353343b63 | -7.02227 | -42.11652 | 2026-10-08 03:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b3d555b9-e545-3694-be6d-3908b0c026e6 | -8.0626 | -44.8052 | 2026-10-08 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 378f347f-3059-3fa0-bec0-dc6fe800f624 | -5.49575 | -42.85772 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 074df2b9-9533-3445-a231-53f0a2c4eb98 | -6.37398 | -42.90379 | 2026-10-08 03:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 686b5029-eba0-307b-b9a1-5879b0510405 | -8.2166 | -46.37806 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bbcdfecb-46d8-3a08-9aca-07a8448e4e4e | -5.71614 | -41.76004 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4bc2ac14-cfd2-3ad9-9970-0c4f70b1b09c | -9.87738 | -38.9976 | 2026-10-08 03:42:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2761cd0a-9a0b-3c6b-a952-97df13114f22 | -5.98566 | -40.9315 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e5315a80-4a9f-3155-838c-b405977d2456 | -6.83123 | -39.55565 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 261aa1df-7ca1-3e45-9cfb-0d92aff044cc | -6.35668 | -42.57399 | 2026-10-08 03:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f6818e08-3bdb-3e25-99a7-46aa6c2d16e9 | -5.72839 | -45.15193 | 2026-10-08 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d4c53a60-dc78-33bc-9e1a-aac06c52a992 | -10.24866 | -36.33292 | 2026-10-08 03:42:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 1446140f-4815-374b-961c-18bd99941d60 | -5.98624 | -40.92821 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2fb44577-1f14-33ed-958c-64da2cb1aa76 | -6.63629 | -43.73632 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| b617cbf7-fc22-3375-888e-68ee0b8d8ab8 | -5.98508 | -40.93484 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1e761cb9-cbe0-30bd-b9b6-bebb48fcef36 | -8.71972 | -45.19997 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7be7eb8-b973-34cb-af44-676d9b8b5414 | -7.21791 | -44.15942 | 2026-10-08 03:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a48db0cd-7849-39e0-982b-ba6a63757ff7 | -7.46784 | -42.84032 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 275c810a-6492-348c-ac7f-50e0f054cc62 | -8.72209 | -45.18776 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cd158a54-5325-3a18-b624-17b51ab5c8a7 | -5.95781 | -40.93367 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cdf05512-c8bc-3591-ac34-d2b38881b52d | -6.63536 | -43.74136 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 1330a22c-60a9-319a-8086-f58b19da188a | -6.88278 | -43.6988 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 17eb7568-fade-308a-b9f5-61c6e9483246 | -8.73012 | -45.14647 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eae2fd3d-b666-3ec5-bc60-21e3418711ca | -8.71321 | -45.19797 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47f748cc-5a87-3f3b-aebf-6d009ac84899 | -5.48885 | -42.86114 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b2e9f1fe-fc86-3562-b3a4-cf55388085fc | -8.73327 | -45.1657 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d8068fc9-192f-3025-8f16-1ec0d98bbc59 | -4.72817 | -37.84422 | 2026-10-08 03:42:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc9be51e-864d-38a4-aa25-8caba680077f | -10.24128 | -36.33163 | 2026-10-08 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d0e90e5b-09fe-3adc-9c45-83192ef81e76 | -6.93126 | -43.66306 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2914ce04-5a79-3337-ad6c-a55231c40962 | -6.62246 | -37.884 | 2026-10-08 03:42:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1085168d-c2ce-3503-a009-bae9e9d80b1e | -6.95368 | -45.26583 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec5f1f65-ded9-3d1c-b99d-c4804c8c341c | -6.82644 | -39.55484 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a7bd720c-71d9-39a8-87b2-0f077a0a3597 | -5.7168 | -41.75627 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d7a09d0c-37aa-3d3f-8869-73fd6f04dbe2 | -5.48022 | -42.87409 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ea562a9e-85e6-3375-90d2-a43ee3d5cfcf | -6.61561 | -37.89833 | 2026-10-08 03:42:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c6b936f-f34c-380e-a55c-ad07c6389f5b | -4.34989 | -43.79125 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6c304ee1-6da7-33a9-8fc5-f42f0af0cd09 | -6.15934 | -39.44452 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 29af2477-3ba6-3ddd-8529-3d182366f166 | -6.15321 | -39.43134 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f56fa1e9-c2b0-32d3-ab68-568825603a0f | -8.7807 | -41.1479 | 2026-10-08 03:42:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 729b4954-a6c0-3bb1-a13a-1ab7250e17e3 | -8.21645 | -46.32861 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa218b22-9a4a-3349-bb8a-2afcff01edde | -6.94342 | -45.28147 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6be6147a-c067-3c01-860c-b4b678c7ce2f | -5.97306 | -40.90947 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 57e47349-88c5-3a24-8984-c7b92dc872d6 | -6.35863 | -42.58429 | 2026-10-08 03:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 94c478ca-6691-3758-b05f-add845e861b2 | -7.19867 | -45.35682 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 24876ddb-1771-3455-9927-da6bcf7d8418 | -7.21892 | -44.15403 | 2026-10-08 03:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fa60582-e340-31b3-93e2-8e452f05da2d | -8.88252 | -45.60236 | 2026-10-08 03:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1060cb2-fa88-3bfa-85a8-62dd9a01600a | -6.82252 | -39.54907 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 02d8536f-b891-3edc-808b-5aadac72942e | -8.71665 | -45.1803 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9b83b1b4-53d5-3d59-a28a-e77de263ef84 | -6.59892 | -37.8926 | 2026-10-08 03:42:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aaf2d344-067d-35d9-a9a4-63d3f14681e7 | -6.63091 | -43.73015 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8cf9901b-e91c-300f-84e9-baf7965aad06 | -7.59977 | -42.3801 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c193601f-f612-3e8a-b452-1e6fb569aee3 | -8.20957 | -46.37599 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 623397f7-2a74-3eb7-8dc4-d9f4fc705c2c | -8.72325 | -45.18182 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e31e68c2-3d2c-3db9-a937-06098e249039 | -6.9525 | -45.27219 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 71f344c2-b01b-3e87-a939-196db17909f2 | -5.98866 | -40.94583 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6eb70fa1-61f3-3ba2-9af7-66bb72511ebc | -8.78466 | -41.1479 | 2026-10-08 03:42:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 84ebdaa2-4a26-3b05-99ed-c6676750882e | -6.97736 | -40.03415 | 2026-10-08 03:42:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 856e468e-60a2-3f40-bc32-68ff1077cdca | -6.88464 | -43.68866 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a039e3c2-a07c-3233-9eea-79add7ee6087 | -4.72634 | -37.84734 | 2026-10-08 03:42:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9f3049b0-fecb-3057-ad74-7dd8a20e5679 | -8.22222 | -46.33713 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d51745dd-d4ae-3cf8-a3c9-7beb12f77310 | -4.68213 | -40.8317 | 2026-10-08 03:42:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e69c2d8c-3776-36ce-a2a1-5023196212e8 | -7.22278 | -44.2766 | 2026-10-08 03:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71f3aa2b-b6b1-31a2-9fb3-aa7774bb924c | -8.21779 | -46.37214 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c67f9547-87df-3681-9323-abb8840dd9a6 | -6.15711 | -39.43746 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 21e31d14-1734-3bca-897e-8fbb2cc8ffbb | -5.75731 | -42.06275 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8829cc34-c681-3410-91e6-d7d60c712b58 | -6.82556 | -39.55977 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ffd2873f-1440-3f14-9558-a5673741161b | -8.59966 | -45.63343 | 2026-10-08 03:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90f8633e-5171-3c2d-b640-6bb48c708933 | -6.98725 | -40.03579 | 2026-10-08 03:42:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bc1d88cf-3059-362c-95e8-33d262c58759 | -7.46467 | -42.85761 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 04bfffca-7920-339b-bfb9-44cf1d296e09 | -6.89091 | -43.68982 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README57.md)
