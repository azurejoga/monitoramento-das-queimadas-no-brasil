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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef166f6e-e1cc-3979-95f9-6dfc3885c0a6 | -8.42612 | -47.25708 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5bfc8986-b9e0-37cc-af6b-e38e068f12b6 | -6.17229 | -41.04185 | 2025-09-12 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e561d442-56e1-3886-8aad-0889ad60a515 | -10.41789 | -49.99934 | 2025-09-12 04:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccd47a4d-c9c2-398d-bb8a-3ec6e2a58e4e | -10.66489 | -48.6587 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adaa8e0d-11d7-3390-bd0c-102a3e51b800 | -10.71131 | -48.62344 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fd59fa3d-f045-38dd-8346-9307089def5f | -8.18373 | -46.11071 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60b101f2-7b3c-3d07-a59f-8d3579329497 | -10.56124 | -51.48653 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c4dddd2-8347-3517-a8bd-7355f6167c43 | -10.56034 | -51.49112 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a800dee1-5da7-3a4f-807a-3361517311a5 | -9.80685 | -47.81428 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcfb931c-693d-3e00-ac69-cba26ec62539 | -10.74625 | -48.18252 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8fd412a-be33-3a16-9984-d24f77fa9926 | -11.4253 | -43.54706 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9c536c86-a2f6-3cc5-80d4-5779e012f342 | -10.87437 | -45.56519 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc1028b1-87ca-3baa-8144-f781508aa19f | -8.19007 | -46.09957 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee9b7c7d-ca0f-366e-9295-6c190ae40cd2 | -12.11666 | -44.8575 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8ec69a0-117f-3972-8ab8-00508cd259e1 | -8.50575 | -45.6534 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b883f016-13be-3615-9b99-507ab98fbd98 | -5.12249 | -47.52764 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a23254ae-ac3d-39b5-a32c-6cd2afbe7205 | -10.3707 | -50.51437 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5563abed-ef0c-39ea-a985-858f18e2159c | -11.17156 | -45.31104 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5003edcb-64be-3916-8abb-9c603d8f99a4 | -10.16823 | -46.16879 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4be875d6-11db-3b83-a80b-d33f88c1058c | -6.52605 | -44.60234 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c095b2b6-9e6f-300c-9d3c-50b24041b626 | -11.69272 | -46.5155 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b2de70-4484-30af-8a08-439776390f38 | -11.43324 | -43.56466 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 453cb0b1-bd02-3eb7-8b5b-84ae8dd62ffa | -8.18129 | -46.10776 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ee82c53-d576-3ea2-add8-797383e83aaf | -9.09048 | -46.94707 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06b4d706-91ba-38eb-955b-99c4648c5dfa | -6.19821 | -42.66884 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 23735c24-c1b5-3240-8ffe-12efc412654d | -9.06568 | -47.11607 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c83e04b-f330-3453-a022-6860c4ac50dd | -6.6854 | -44.13534 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73e2eecb-e286-3b0a-b4f0-323493fe9798 | -6.27108 | -42.42286 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27192fa0-2583-3182-b62d-8d37cfd685fd | -6.63801 | -49.78348 | 2025-09-12 04:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5b8a8a5-b8fa-3d6b-8d09-9479dc0b5919 | -11.66707 | -46.60153 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a000e522-e24b-3141-a8c7-cb4324a3ed2e | -8.87926 | -49.53868 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1d45be4-6d8e-3074-be72-6b37ed53a79f | -11.47001 | -43.60229 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5597765-5c6b-3582-94af-397f09427a67 | -9.72828 | -48.09212 | 2025-09-12 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a4b98d0-4be2-3ad2-b314-fd3a8c6411c7 | -11.67571 | -46.60989 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 71238266-dd22-3d3a-9a68-c9caf77c09e9 | -8.18322 | -42.42913 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| db08f527-4377-311f-9d46-e5a243e19284 | -7.29968 | -44.35731 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba3ebe3e-f626-3fc2-af22-8e916ce30194 | -11.73722 | -46.52808 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cf26c36-8574-3b9c-a3ef-268e789049b0 | -9.03433 | -47.11049 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38f8e6ec-7850-3dfd-8141-7cd4dd6dbe1f | -10.12612 | -47.90845 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cad77c45-9767-3d11-ad3a-d22a625aea82 | -11.14753 | -45.31216 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66e30f2f-8015-3973-b521-4e0ee6a9aa6d | -7.75653 | -44.76387 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13d9aeaf-d786-3028-8b92-c48455d3d8ac | -6.10612 | -45.93389 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b508d73-02fb-3b51-a146-a803b6b857b1 | -9.03621 | -47.07369 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| be11d428-bfd2-309c-9454-83fb4156ab68 | -7.86104 | -44.83873 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddf12d8b-54c3-3289-af0a-769cfd300a4a | -7.155 | -44.34048 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e6524ce-ad75-3512-8d03-066123722109 | -6.30391 | -42.22017 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6684ab2b-e736-344c-acec-d77967952194 | -11.14794 | -45.24196 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18178e07-175e-323e-addf-ed9e47cfb347 | -6.30095 | -44.58168 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b5ff11e-a0ec-3f66-8f6e-dd76fc8b83b0 | -6.99821 | -44.7799 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7167f13-dc92-3ed0-956c-262ff3566f31 | -8.94607 | -46.71642 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b86be437-dff5-3f8d-97c6-8b8a82ac7a6b | -6.27146 | -43.22534 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ade55905-6cad-3c14-a7a9-06b2372549fe | -11.67085 | -46.58946 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e83c8008-cf1c-371d-9aa7-93697bf75d57 | -10.40148 | -39.47889 | 2025-09-12 04:04:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 11ff90d6-752b-383a-a039-c85124fed3a8 | -5.404 | -45.9368 | 2025-09-12 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 155af7ca-6414-330e-ba93-d4f2354743de | -6.34175 | -43.04406 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04655110-5d0a-3751-b795-74465c64f751 | -10.38437 | -50.50213 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a4cc93f-93a7-3eee-ad4a-17248aed42cf | -9.88274 | -46.4639 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32628c98-d891-37a1-8578-5ad67dbd08e9 | -10.14002 | -47.91106 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92d5453c-ce59-35ce-b862-3b4d76634b03 | -12.11741 | -44.85319 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a219289c-49c9-32f5-8753-f715a66a6543 | -6.59597 | -41.44867 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d58fe14-3079-39a2-ba43-00af44b8b8eb | -8.17113 | -46.09037 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a3cb203-2685-32ae-8e1b-14172e1db80a | -11.67148 | -46.55149 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03e8f643-0fb9-3f11-a71c-8f1198a99d5b | -6.683 | -44.14949 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4b71272e-6416-308b-833b-5e9d1479c3c7 | -9.87703 | -46.47152 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e98588c7-fc2d-3960-ac69-d7b050c11c92 | -5.69628 | -49.2002 | 2025-09-12 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b66721e-d393-3487-aebb-22edaf59cc10 | -6.96502 | -44.83215 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b66fceef-091e-34b4-9ed6-c29ba4560978 | -11.73789 | -46.52427 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b1df9fa-4dea-30af-a463-cfc537a5bf92 | -11.68465 | -46.58401 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 171b1d80-97a6-35cf-8886-92fc7f10cc7d | -8.37363 | -44.83926 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 862db682-9e62-3ac0-b399-6658a418e224 | -7.4041 | -44.36434 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4ef43b1-8b5e-3523-87d2-63bd1f03d4fb | -9.44493 | -46.41809 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 726c5b8d-074c-30e9-b5fb-1d89ed535f2c | -6.24659 | -43.42542 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 719df8c2-aa4a-3182-a5b9-9db72b8ea087 | -10.74159 | -48.1816 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 959cd22e-7a2a-3fcd-bd94-f5a7fec1c511 | -11.09996 | -48.40187 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88cebe29-fbf1-342f-a8b3-6dcc55f4b17d | -8.89817 | -49.9376 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1913f9b-4c92-31ac-aefa-6bcc2206bbcf | -10.08133 | -48.1719 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78bd037c-2c22-3f5d-b3cd-be37b7e0d709 | -6.54027 | -43.10831 | 2025-09-12 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f87f280-0877-3d22-b4a5-995360905e02 | -5.94793 | -42.7848 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b3e6c53-45f2-3e0c-b118-48c8bd1a206a | -10.35083 | -50.52917 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef4168ab-89fa-3a94-a3ef-5025a736ecb6 | -5.65526 | -45.941 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ee27755-77de-3e52-a4c3-ebe710f46d08 | -8.17047 | -46.09426 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 008909af-8b27-3819-9a56-3976c22912dc | -9.72303 | -48.34172 | 2025-09-12 04:04:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22f61fe0-c9e9-3103-a3fe-21ea338b0c7e | -11.67501 | -46.61378 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e2832373-7342-3ea4-88e7-3c33d3b73c97 | -10.84867 | -48.17078 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 31f569d4-aae6-3de4-aa13-7a1bfcd424f0 | -6.81459 | -52.80931 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd31d1d2-2ea8-384d-a940-e6f0ad8c0444 | -10.6853 | -48.65639 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08bd76a6-d17d-32fd-94d5-e904fa9daabc | -10.13933 | -46.30928 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a34b0267-1281-342d-b434-2abb416acfcf | -6.88407 | -44.21729 | 2025-09-12 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cc3d0c2-96c3-3856-9107-ec14b1feb307 | -6.47833 | -45.15879 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4714a682-fdca-370f-9fac-88e96231330e | -9.01909 | -45.76448 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc604c27-d8bd-3415-9f4c-be3c15de6d3d | -11.46801 | -43.61426 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2187bcb5-7f1a-3d66-94c4-e5a005b87c03 | -9.68356 | -47.5533 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a90a9a7b-3156-302c-8140-c29a7d94674f | -8.17976 | -42.42854 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 99354e0a-f57b-30a8-8e10-3985876e521e | -9.0993 | -46.9488 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6465d5d3-4a4d-39bf-abdf-9fd32ffa16db | -12.1532 | -43.70682 | 2025-09-12 04:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c29d6561-7ee1-3d0c-b53d-960a4d0a61e3 | -6.55181 | -42.40612 | 2025-09-12 04:04:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8a2c488b-468f-3bf0-a7ea-c119d423f79f | -6.45062 | -41.7652 | 2025-09-12 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c2b5c1a-6d64-397d-8735-e9ccbecbf6cf | -9.16186 | -45.56509 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c06ddd3e-0ea4-3b0e-a1f3-85a12f5dd61d | -6.56694 | -44.21218 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e12f3f3-9dfc-3843-998f-1d7a513b9ed7 | -7.69723 | -44.69123 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README39.md)
