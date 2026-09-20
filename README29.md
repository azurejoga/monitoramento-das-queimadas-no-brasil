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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7e9c83b-91be-30f4-8d45-83859200a7fa | -4.68406 | -46.40645 | 2026-09-20 04:19:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4fb65106-e135-3146-a025-fe0cd3f4c1cd | -11.45684 | -45.70858 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b2fc5d0-be36-37a5-8f2a-17f1eeb53d90 | -8.45378 | -45.86659 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 713e7ceb-1df5-314a-890e-9f27af445225 | -10.46137 | -45.08004 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4de6af8b-8024-3939-a9aa-e03514c6d41e | -5.45565 | -44.31485 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f24996b-04f3-3dc0-a679-14727c2fec28 | -5.85289 | -53.52742 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5723cb94-2c5b-3dc5-b5e8-65a7b9399dc9 | -8.37409 | -47.19537 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00bb6d8b-6313-3069-b681-e1bb0db76ecc | -7.31606 | -55.6151 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 705a4067-9474-33cd-8a79-f96cb456a99c | -7.53128 | -45.44154 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9bdc9bdf-03ea-36cd-ac17-350995a6c397 | -5.62252 | -40.85413 | 2026-09-20 04:19:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac34fd0c-b463-3b10-962f-d2de446988e1 | -9.25941 | -45.92776 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48a67366-cae1-3bb9-9280-fd2deb5afdf2 | -11.0872 | -48.30317 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 65908845-7828-349d-8133-e1d6b939837a | -9.22286 | -43.18313 | 2026-09-20 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8111452-61c7-366a-be0b-813f9c903ff4 | -6.92366 | -42.91211 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 42c1e5a1-90f4-3731-b827-2255d54a3365 | -10.28048 | -50.27429 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 50576569-5aec-3d27-947b-00e8b2161174 | -8.04799 | -46.25417 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a47dbf5c-30a3-3d10-85a6-404ea121dbab | -11.31607 | -47.27872 | 2026-09-20 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e47a3f89-37eb-383d-8d77-457bc92a3b20 | -9.7909 | -45.0771 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 185c0375-8ce2-3d68-858f-4740a32e5b52 | -3.45254 | -50.5999 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35d2d43e-09a8-3043-a965-77e1c9623dc9 | -11.9779 | -44.99368 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4078c47-98a5-31c8-b9cb-05b04f79fd98 | -8.38933 | -45.62608 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ecb25f9-975e-3a14-97b9-18781cdb186b | -11.12999 | -45.2959 | 2026-09-20 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 921390e5-bbec-3ee8-8c92-30c991abdd79 | -8.18216 | -54.73829 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9fbcd8c2-4470-3c74-9866-23cca079887b | -9.78446 | -45.07183 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63ea0c37-a6d8-3d56-ab99-b2d75ede3445 | -7.86489 | -44.84942 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0aea56b4-7ce3-35b4-8a32-b5b231722961 | -7.01437 | -45.2509 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| deb7cd0c-c742-38aa-b33e-5ec840899ae9 | -6.19338 | -45.32892 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0be28866-36ae-3ced-94cb-8d315ce4aa11 | -11.45396 | -45.70383 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc305669-bd3a-3818-8199-73f5ef17df9b | -5.87236 | -52.04324 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7cc4202-044b-3c35-8b84-2d93b5f019a5 | -5.62863 | -43.38045 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30a8d368-94bb-3dc4-b9a8-9dba82c271a1 | -10.27471 | -50.2508 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 87fa8796-32e3-346b-a130-ace1b41ccd99 | -5.84505 | -53.5696 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54899f13-6709-30f1-be7d-969c79620f67 | -9.54694 | -46.58485 | 2026-09-20 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bac033d8-7007-3319-8f1a-c9b1d19b677e | -8.77784 | -48.72953 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f3878b40-2241-3ab5-acd5-ba1f17f65bb8 | -9.27801 | -48.24216 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fde9ac4-31c5-3776-b4e2-c8d0497db2ed | -7.12307 | -43.10278 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aa44f3c3-5c5f-3257-a534-693d8f0adfa0 | -3.46124 | -50.61651 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 798cfe72-ac2a-3c9b-8b6f-1f2c4559d9ab | -10.41308 | -48.90847 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acf19177-a6c6-319a-8d4c-40baa960ac29 | -5.86848 | -51.55906 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1973ab4f-6bb7-30c2-b763-a29a7686a3ef | -9.03606 | -49.83159 | 2026-09-20 04:19:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2b67865-4f64-33f1-b8f6-31c468c39745 | -6.75478 | -47.9229 | 2026-09-20 04:19:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35772a9f-6a7b-3fc4-a0e8-8f41fefcb0ea | -6.2847 | -41.77379 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bfe685ed-5dc2-3bc8-a731-4872f386139e | -10.31167 | -50.25333 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 749ae0fc-4136-3a91-ab2c-7497e9eaa54c | -11.45372 | -45.38891 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5075f7d-4cf9-3f02-b325-4f05b301ac99 | -9.93559 | -53.98754 | 2026-09-20 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef845c26-d046-30cf-bd8b-d72ca6959c13 | -11.45467 | -45.69967 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3e421fb-2b3f-3976-8643-a97c26e85fba | -8.29686 | -46.84685 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cce59bc4-05a0-3e69-8e72-66d9f541d323 | -8.76443 | -48.66342 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 483d88bb-87e1-3c14-b222-576529acfffe | -7.09181 | -42.08104 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3c6730df-60b3-346b-af4d-8633048efb52 | -7.7403 | -44.68225 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6eb2c078-e697-3ee8-a8a5-503f246d0dd1 | -11.03442 | -48.30716 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 212664d7-39f0-30b1-914e-804be4f83aad | -7.69578 | -46.10656 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bb8bcd9-94c5-3372-86be-ca70e49c0ed6 | -7.53574 | -45.43773 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 25c5da04-3999-3b6c-8f98-52a0d10d369a | -6.7812 | -48.66026 | 2026-09-20 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb9d8b26-d34a-3dd8-b7d1-6d8dbca13760 | -6.65161 | -47.73841 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63f7f4e8-bd5a-36c8-a2a9-052850f07e6b | -6.17049 | -47.71305 | 2026-09-20 04:19:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccbb10cd-7c52-3ca0-b427-dd7fd5d11c3b | -6.32299 | -47.63379 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 174b8f65-7b3b-3fc4-b1d9-59f960b1d1d7 | -11.42992 | -45.42206 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee55be92-7d46-346d-afd6-c9eef9815758 | -5.85882 | -49.79084 | 2026-09-20 04:19:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bee8b17-f758-3d87-8581-9e6ed4c6a53c | -7.17031 | -47.44666 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0c6ed2d-e452-33b8-b576-00f485a5509c | -11.45826 | -45.7003 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b75b4f20-c46a-33b5-bc7f-b9961b7f943d | -11.45325 | -45.70797 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4b396b8-b348-313d-88de-194b4ed49939 | -4.98648 | -45.15127 | 2026-09-20 04:19:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab8f6bb8-50dd-3702-9336-ac3af77c9b37 | -9.8916 | -46.53725 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da3658f9-86ee-30b9-9e06-cd50965a4f2d | -9.77157 | -45.06136 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 209b4e20-2220-3474-99f7-e87a9b6a8c5c | -8.66837 | -45.43154 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86e07bcb-eb01-38c8-a539-50c1d13fce3a | -9.0469 | -48.71868 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d2c1e47d-6ce1-3da6-a354-fb669f49d7e0 | -8.17095 | -54.7482 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39c8e6dd-d680-38ce-8451-79f9508a1ed6 | -7.32802 | -47.43809 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c0fd708-f986-34fb-a5f3-35f8daf2c736 | -8.60987 | -54.59478 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 100523c0-e41c-3065-b860-1dbd4b726cad | -9.83738 | -46.43921 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8345e887-ed48-33d3-b7d3-a34449104992 | -5.64772 | -43.3719 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d056c67c-e7b8-3709-ad6c-78471784791a | -6.18079 | -47.49636 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee03c3e4-0a03-3f09-a8d5-555dea77e21d | -3.95836 | -49.04315 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1ba949e-4a6f-32e3-ab59-52a1d618f820 | -10.58228 | -46.53831 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6cfff0a-9c2b-39bf-9674-39996938af2d | -7.96675 | -44.07624 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10146ff1-a0fe-3a87-8b14-c2c97ab9a795 | -10.19943 | -44.14098 | 2026-09-20 04:19:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07c9a191-1f55-384e-b68f-cf717b708e16 | -11.07316 | -49.49979 | 2026-09-20 04:19:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24cf7920-ad1b-36b0-ab1b-f65e0066a51e | -5.87313 | -52.03892 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13750f87-9088-37f2-a280-1a1420347e5c | -9.90306 | -45.09914 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adf11675-1dc1-34cd-afc4-55c96639d769 | -6.20171 | -45.32541 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c0b65dea-f2d9-34e1-a4a5-75682a2d7772 | -9.70612 | -54.83538 | 2026-09-20 04:19:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af1c27a7-d716-393f-9e20-9bda15865dc7 | -7.77036 | -44.83441 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9be2b3dd-d0b9-36f5-a1c6-d42c8cc0865f | -7.52275 | -47.33544 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 035b8581-d42a-368c-a8bd-022267afa16e | -11.482 | -47.75514 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3299d119-99c4-39f9-9ee6-26aa5918a4a9 | -8.47427 | -44.50257 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8557d4bf-8dab-3b77-b92b-a9609bc87963 | -10.57472 | -46.53676 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4101560e-4ea2-3f97-abe5-1d36ebe52a3c | -7.56836 | -45.40227 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bdd156f-2781-30e3-9480-67303424f15f | -6.7195 | -46.07647 | 2026-09-20 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f5f0efa-5ef2-3e7c-9e09-eeafcf3b4269 | -5.66879 | -43.40605 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc7fb466-1f54-3cac-a58d-bf4f12b2d6a1 | -6.00656 | -51.7872 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5db28897-2280-3d1b-ad87-041a289f590f | -7.15614 | -47.42781 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45b482dc-f988-38e0-8357-5653925c7bc5 | -8.75548 | -48.66182 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ff55dfe-1f37-397b-9000-d82c26b29034 | -10.54464 | -46.73343 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f649190-d7dc-3ffa-a099-900f8dd16369 | -11.45152 | -45.38026 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f28408c-d190-3e82-af9e-17c51e5e4fb1 | -9.54292 | -45.40105 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6fe90ea-d7c9-3cc9-b545-0390d21b92a3 | -4.80852 | -45.7733 | 2026-09-20 04:19:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63e90c1a-4467-3fc4-b53c-ca90c8a511ea | -5.45857 | -44.31961 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e225d23a-2d1a-331c-aec3-054f86d0eb70 | -11.32576 | -44.17804 | 2026-09-20 04:19:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 525cbeb7-370c-3600-abd4-1847dc90416e | -7.44005 | -44.75386 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README30.md)
