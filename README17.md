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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 018770a0-e2e6-3a58-982e-9a6ed0dd8c70 | -9.05293 | -38.95266 | 2025-10-12 04:14:00 | NOAA-21 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0f49352-e314-3379-948c-b4a59237ac27 | -5.28571 | -42.54026 | 2025-10-12 04:14:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65955127-a323-3f40-b7d8-7b7aa233f755 | -7.14174 | -42.50549 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 12e1fd5c-cf7e-303c-a6c0-bbdfc8a113fd | -7.70218 | -42.37743 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b9b9eae-fdb1-373c-9eb4-b958d4449846 | -7.54515 | -43.84242 | 2025-10-12 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54b91ba3-a17a-382a-95c5-2c579502b031 | -7.28653 | -41.96431 | 2025-10-12 04:14:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 750bd471-16cf-3f0c-a61c-50885e9aad8c | -7.42737 | -42.96668 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0340f37e-71cb-379c-9c9a-365609adb447 | -6.66866 | -44.6076 | 2025-10-12 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ce75434-c92a-341c-b30c-bb3a024c5d71 | -7.8102 | -42.42663 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7bdd9df8-bb99-390d-8bc3-9518d25a73bc | -8.85574 | -46.0418 | 2025-10-12 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d22b3542-337c-343a-a9d6-cfadcfc40888 | -8.90667 | -38.41165 | 2025-10-12 04:14:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 809bd4a7-9dd8-35ce-a41d-cdbe29333c60 | -5.94285 | -44.20342 | 2025-10-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c9811f6-3e48-3761-9ff5-3a6db6aaf8c0 | -3.19413 | -52.23292 | 2025-10-12 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ba0bab3-9369-3531-b4f4-ceb61cfba540 | -6.31535 | -41.59919 | 2025-10-12 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| db0b70ea-899b-375c-b7d6-7152a4ce6940 | -9.40764 | -45.76378 | 2025-10-12 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f384e5a-f47d-3bd9-b752-9db6c180f231 | -5.58279 | -42.98867 | 2025-10-12 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d81ecd3-3598-3b51-a6f5-d5b9e80debe2 | -5.36113 | -46.29026 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e6408c0-e94e-38df-a8a6-74492a8189d8 | -5.81945 | -44.03576 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c5d103d-d05d-3e9b-b5fc-3c44325cf5ba | -4.47584 | -44.92044 | 2025-10-12 04:14:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4f7d670-abf8-3439-a92d-0d9ec3921737 | -7.80192 | -42.43616 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c6638745-b595-3b3a-978e-62bd43260784 | -6.74433 | -42.80581 | 2025-10-12 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fd098e0c-eb42-31bf-bd28-7c6c6f619407 | -6.39918 | -43.44664 | 2025-10-12 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6845eba-592f-3b63-b9ec-e261465f453c | -5.82944 | -44.03732 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dab2670f-8f12-3966-a0dd-08f7be6f21ca | -5.35012 | -43.43208 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c19645dc-92d2-35aa-ba23-cbe39585f5bc | -8.22268 | -43.36589 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2135fb1-2e1a-3506-989d-c3348c0fda87 | -5.8178 | -44.02469 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe067626-ddad-31cf-a790-c7d8986a2985 | -11.35636 | -43.99883 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d00ff22-393c-345f-854f-391f5c905890 | -7.42758 | -45.16124 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7718157a-b76e-31ac-85f4-7b9ade498f77 | -7.05442 | -45.25407 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 535e7d97-8a7e-3f90-ae1b-b951fbdfccfa | -5.61324 | -42.57775 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 306ad108-873f-3db3-87bf-4a782dd80b64 | -7.51267 | -44.60677 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbec6333-662c-30de-b5cb-8816b37fda1d | -11.91597 | -44.18251 | 2025-10-12 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b9c3b73-82e3-3f23-97e3-3d4168cc919b | -8.22046 | -43.35846 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd10e953-e496-30ec-a6a3-cf2d19f63e2a | -7.1533 | -42.49656 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3aee89fa-7e55-33a6-b8c5-b2d85e9d646f | -5.91998 | -45.42216 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dec0d5cf-cb6a-39d2-904c-f625f60c1bcf | -4.46078 | -50.09819 | 2025-10-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cd0f585-112a-3774-b512-2ee089c813ec | -11.91651 | -44.17901 | 2025-10-12 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a098b681-3c66-32dd-8495-8bde0e7d09e4 | -7.91144 | -44.96857 | 2025-10-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ba433d0-dd77-3b5d-ab9b-b4341ac45d3c | -7.01759 | -42.0975 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4907125f-c5cb-3be5-9777-81c1e7316c57 | -6.58582 | -45.92635 | 2025-10-12 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2592367-0928-3b88-b50a-f4c3e20cfc88 | -8.21986 | -43.34064 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 368439a1-40a3-30a1-9d2f-c9472554c54a | -6.78801 | -44.52024 | 2025-10-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdec48fc-9c69-356d-b1ac-be00696244f8 | -7.0148 | -42.09341 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 84e99009-5668-35cd-9f7f-52dc544aec77 | -5.7444 | -40.76477 | 2025-10-12 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73e0ab33-fdca-330d-870f-a56472d3c49f | -5.82326 | -46.35605 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 228efd50-3a2c-3d24-9fab-7322b9850efc | -5.91525 | -45.42934 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 68723224-d260-3c2b-b123-f8215c14c1f2 | -5.40031 | -40.97028 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 859d94be-eaef-3afb-ba06-eba8108f9327 | -5.94563 | -44.20749 | 2025-10-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d97ac9ee-4f7c-3cca-9aac-1b0044a421dc | -11.75363 | -43.31813 | 2025-10-12 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e456e6c-70c6-3b60-9bc2-68d10dcacf1a | -6.28449 | -44.40693 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea62c326-1d87-3a31-b5e2-9654cf41b09c | -11.75473 | -43.31099 | 2025-10-12 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd594810-f7b7-3225-a8c8-c639d19484b1 | -6.76771 | -42.83419 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a1acbe14-5969-36fe-b972-cc90cc87e42d | -6.75745 | -44.6478 | 2025-10-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b4cf71f-bdbd-3366-bd2b-0a48190eabc7 | -6.39588 | -43.44613 | 2025-10-12 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 178f5eed-d70d-3482-abff-8421e010d716 | -7.01992 | -42.74298 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b6316fac-9413-3d10-9170-9ba7dd1b20af | -9.52525 | -47.86794 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b35d15fb-901b-3004-8c78-a02115f4fc5c | -7.12805 | -43.27275 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e97caa7-ce97-37f8-ab26-f72570570ec1 | -6.71437 | -42.88949 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd81df91-833f-33ce-9ed4-8445a667fa00 | -6.42264 | -42.53543 | 2025-10-12 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f0defa6c-3676-3384-824d-71eeb9c8412e | -5.7492 | -44.28896 | 2025-10-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c69162e-b84b-338b-a43a-2824a242fb10 | -6.28392 | -44.41051 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9efe6d0e-27d5-30c3-954c-6bec6a66a5c3 | -7.13735 | -42.51196 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 79852a94-2178-37b5-97cd-618fe112a9c0 | -7.49553 | -42.76778 | 2025-10-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8bd44300-035f-3501-9079-c2824bcd3447 | -5.09488 | -42.60545 | 2025-10-12 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f5e2ba-c358-363d-8799-201a59034407 | -7.26501 | -42.95831 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec0eaafb-0a54-3de2-91cc-386b14fe50fe | -5.50086 | -43.7905 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 646ddaf2-e5d8-302d-8be5-96d8ad545540 | -8.77065 | -47.29266 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7be53349-c2ba-3ac5-ae34-1506d0dd0efa | -6.98956 | -42.03505 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3ad11183-4f1a-3f6c-b59f-fc8de0cbeb73 | -7.14568 | -42.52394 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4111a9e3-1ac9-37a1-ba09-7405a1b3ab1c | -6.25481 | -43.0211 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a2e8e98-bfc6-319e-9c61-de197ec18fde | -11.67281 | -43.77668 | 2025-10-12 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9efb023c-5a14-3036-beb4-73084f3621c4 | -5.59748 | -41.1084 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b51d6550-13fa-3eb2-9ded-b458f2655ef1 | -5.60994 | -42.57723 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88c31c4a-d51e-3994-a0c3-da8db6341a81 | -6.24331 | -43.02987 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3b28d0e-cc16-3047-b7fb-a03adcc2cbe5 | -8.05063 | -44.11196 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84414562-add3-371d-8200-a12cc160ed9a | -6.76326 | -42.81938 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7a8049e4-4f31-3f04-8209-6f5ec044580a | -8.0267 | -44.45695 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df8c9fc9-69d9-3f8b-b9fe-20fab8cabe87 | -5.63233 | -42.69356 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17ed9a45-e58b-3666-9e91-bbde9c394d7c | -3.85125 | -50.76829 | 2025-10-12 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56dd0d3a-881b-38a2-8f16-1eb148fe50a2 | -5.65516 | -42.78513 | 2025-10-12 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5eaef5b1-8b9c-30a7-a486-d0c23cfabc92 | -6.31841 | -44.25931 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd614ad2-8273-3f9d-85cd-3f35d84fd589 | -6.24647 | -41.56312 | 2025-10-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 793e2844-534c-3379-aa37-7971ec5abd33 | -5.49117 | -42.90026 | 2025-10-12 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 47b13a5d-17c1-3d6c-a5ab-b8e505d92f8f | -5.46452 | -43.39705 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d389a660-985d-3f3d-8af0-4e7fba1cc05f | -5.31877 | -42.89039 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f7bdc60-d381-3afd-a126-9be1604ee401 | -5.82667 | -44.03328 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90f5fa4f-f406-3773-affb-9e615f2a7b5f | -7.51994 | -46.54342 | 2025-10-12 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74c457de-ac97-3980-b3d1-eaac2ebf97d0 | -7.67581 | -42.57119 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f7ead68d-f7d5-34c3-a3e1-e303a783f473 | -6.75114 | -42.81039 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 35dc28cd-0795-343d-9c59-5cfd5440f6df | -11.36792 | -44.01143 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 043be60f-0d53-3ab4-8b05-350b363f68c8 | -5.09818 | -42.60596 | 2025-10-12 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2f9a6e1-0c99-37ad-84f3-deb4d3d0b9cb | -5.48732 | -43.07572 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 816b2ad2-f008-395f-8899-a78b74debe88 | -6.73113 | -42.08212 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9de79f61-5c55-3325-aa71-568401c77f67 | -6.96221 | -42.43438 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ab01a109-5bab-3e65-8cac-444b5410c938 | -5.48103 | -43.39964 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b46de7e4-dbd4-3c5a-8fb7-1fd2b10cc2c4 | -7.50311 | -45.13144 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bf577a6b-15d5-33f1-ba42-8352e904bb9b | -7.20922 | -45.49095 | 2025-10-12 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f41f2e1-3d89-3468-ad1e-c967d3e78e26 | -5.59658 | -41.10817 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b928d4f-1613-3c1d-a012-6f6007d31cfd | -9.51771 | -47.86666 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe612253-4875-3d36-86f0-88bf5d783d27 | -8.48012 | -46.19871 | 2025-10-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README18.md)
