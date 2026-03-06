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
| 227f1e6e-1911-3b30-9d5b-f2d70596140a | -24.0526 | -49.56661 | 2026-03-06 04:01:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91563143-9847-37e4-8192-332c0c1426f0 | -24.0517 | -49.57099 | 2026-03-06 04:01:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b242ac1-9812-3dd5-97a8-26d30c6ca638 | -23.72951 | -48.7789 | 2026-03-06 04:01:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf82ab14-1902-334d-8046-43ce3feae966 | -23.27313 | -51.20739 | 2026-03-06 04:01:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b6cca2c0-4d1d-34c8-855e-d7d42a05e5a3 | -23.09047 | -52.35763 | 2026-03-06 04:01:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba1181b9-66ac-3196-8080-9d0b3d06224b | -23.73 | -48.77786 | 2026-03-06 04:01:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 043e6a2d-dd09-3c3c-90fa-b01fbec048bb | -23.85183 | -51.73866 | 2026-03-06 04:01:00 | NOAA-21 | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 89646da1-6541-360a-a328-0183a39f7324 | -21.92957 | -50.6617 | 2026-03-06 04:29:00 | NPP-375D | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 89390f2d-1b13-3e07-85bf-a22ee186ca4c | -20.20235 | -50.64859 | 2026-03-06 04:29:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 42404841-60f3-3908-be26-f81af4101d39 | -20.20468 | -50.65175 | 2026-03-06 04:29:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5ae58ae6-7c92-3fc5-ac35-87d4f42c0e60 | -19.23915 | -52.35026 | 2026-03-06 04:29:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad6dda07-31d5-36e8-8cfb-ad88b906b5bc | -20.20163 | -50.65277 | 2026-03-06 04:29:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 848b03f1-1337-359a-8ebc-a959f4e0b0d5 | -20.56173 | -54.65754 | 2026-03-06 04:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92d1e4ae-b16a-36ab-9ea8-8a0948e57d37 | -21.92612 | -50.66099 | 2026-03-06 04:29:00 | NPP-375D | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a09c44c0-531c-3583-8ebc-170cb667eacd | -19.1703 | -47.359 | 2026-03-06 04:29:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90349d11-6896-309b-a080-4e5fc86f014d | -21.70967 | -48.43527 | 2026-03-06 04:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95761120-88d2-3371-899d-32221fd5f481 | -22.92378 | -48.61399 | 2026-03-06 04:29:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22b553f4-d7db-3085-9dfa-baa457b5d812 | -20.2082 | -50.65242 | 2026-03-06 04:29:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0bde954b-2dd0-3047-9438-b49d295cb5e0 | -21.70634 | -48.43467 | 2026-03-06 04:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76c27bb9-d45e-322d-bfff-1ab9e4c826c3 | -20.20515 | -50.65345 | 2026-03-06 04:29:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ba4d49e4-cbe0-3b02-b2cb-660fafa93d29 | -21.2967 | -49.31982 | 2026-03-06 04:29:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20ccbdfa-1787-391e-b6a7-d2c3eb1d9e3d | -21.28502 | -41.80947 | 2026-03-06 04:29:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 80918e93-5fa0-3191-8d3e-0e08728cabd2 | -19.67142 | -49.33815 | 2026-03-06 04:29:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88b78eb9-9caa-38b6-8226-6ce0219ac4e7 | -20.30534 | -49.58368 | 2026-03-06 04:29:00 | NPP-375D | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfee49b0-ca7b-3812-add2-2ffa05fb9cc8 | -20.91356 | -50.53143 | 2026-03-06 04:29:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f2155440-8265-31a6-ae1a-da6d5aad1a36 | -18.97297 | -51.86596 | 2026-03-06 04:29:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8b4c423-d414-3587-8b35-0f3d82579b42 | -20.91704 | -50.53213 | 2026-03-06 04:29:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eca5d1d1-5d72-3dd6-b056-615286ddd44c | -19.1417 | -50.60291 | 2026-03-06 04:29:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5ed6a838-ae33-3b48-b268-940ab45eb838 | -21.32828 | -48.99974 | 2026-03-06 04:29:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5f437cc-1551-308b-8294-fd05dd5be84a | -22.92889 | -48.60335 | 2026-03-06 04:29:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b140e2aa-ba1e-35da-af58-e50548211226 | -21.19826 | -48.61221 | 2026-03-06 04:29:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d1633811-6cfb-3d51-aed8-c6fd75ae1646 | -22.92437 | -48.61024 | 2026-03-06 04:29:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0771add-b8db-3695-8ede-4ff595374e01 | -21.71299 | -48.43588 | 2026-03-06 04:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95d7c55c-f8a5-3562-b0f5-b4cfa5c34b8c | -21.29334 | -49.31918 | 2026-03-06 04:29:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 330e46bd-cad6-3b7e-9711-438db5989b7c | -20.30195 | -49.58303 | 2026-03-06 04:29:00 | NPP-375D | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26e0f26b-fbc2-31c5-bc90-e374af203729 | -19.67089 | -49.33886 | 2026-03-06 04:29:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f460c3f4-b382-3c42-8723-ff2b41abf986 | -20.24992 | -50.74713 | 2026-03-06 04:29:00 | NPP-375D | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2fb56e4f-a184-3c5d-a035-2c75ad134040 | -21.30009 | -49.17255 | 2026-03-06 04:29:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cf310971-21ad-3b31-bf31-5526dc73a442 | -21.19585 | -49.18853 | 2026-03-06 04:29:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b023d60a-63fd-35ad-bf5d-4781678882c1 | -24.12288 | -49.82603 | 2026-03-06 04:31:00 | NPP-375D | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3b301d10-1cb9-3d26-a28a-630ada8f6d45 | -23.2687 | -51.20692 | 2026-03-06 04:31:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 98882941-9a60-353b-9c48-739cd9fe9338 | -24.0532 | -49.56927 | 2026-03-06 04:31:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2f0d5e41-f5ee-350b-a741-28f5388635b0 | -23.09121 | -52.35958 | 2026-03-06 04:31:00 | NPP-375D | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4e708643-cf1d-3abb-a2a8-3f11b0d841db | -21.66282 | -56.33041 | 2026-03-06 04:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc8b820d-22e1-3954-8c98-226c690f79a9 | -23.79085 | -53.3217 | 2026-03-06 04:31:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 560149f1-79ca-3a88-b2d6-47a7553f111e | -23.72966 | -48.77734 | 2026-03-06 04:31:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1e372c6-5f96-3f13-9746-56ddb41fd83f | -26.10066 | -51.06425 | 2026-03-06 04:31:00 | NPP-375D | UNIÃO DA VITÓRIA | PARANÁ | Brasil | 4128203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bed60941-f606-3361-9742-2d0399c7b925 | -24.05654 | -49.56991 | 2026-03-06 04:31:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3e4cc598-51c4-36ba-b282-635b35903f58 | -22.68241 | -51.28798 | 2026-03-06 04:31:00 | NPP-375D | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 066321fc-4a02-3188-911a-ee5c0f0472f0 | -24.05382 | -49.56549 | 2026-03-06 04:31:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e8f11a6-370c-383d-a1fc-500febdbb3c7 | -23.70307 | -46.36782 | 2026-03-06 04:31:00 | NPP-375D | RIBEIRÃO PIRES | SÃO PAULO | Brasil | 3543303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 869c87c2-9b25-3350-99d8-d78fc37ceea9 | -23.25653 | -47.48123 | 2026-03-06 04:31:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b6c946f6-2e39-3dc1-b78e-19544dba431a | -23.74902 | -46.37121 | 2026-03-06 04:31:00 | NPP-375D | RIO GRANDE DA SERRA | SÃO PAULO | Brasil | 3544103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e1cd746b-f11c-3134-bf18-829873e6e75a | -21.66396 | -56.32494 | 2026-03-06 04:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10b16254-56be-348a-80f0-9046834b5bf0 | -23.27218 | -51.20764 | 2026-03-06 04:31:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b936cdf0-dfe4-327d-b7b3-4d02e1e941a4 | 4.97318 | -60.2698 | 2026-03-06 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5a2ac91-199e-31dd-af39-2d505d38df46 | 3.25717 | -60.74589 | 2026-03-06 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c21988c-9b64-3c9a-925d-a5cc2bb3f797 | 4.97017 | -60.26781 | 2026-03-06 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f3caa73-2391-3b54-a69e-ac000a287a86 | 3.9992 | -60.16448 | 2026-03-06 04:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3435475c-e5a6-3ee9-8934-a1d574b89eae | 3.99852 | -60.15968 | 2026-03-06 04:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 182427cf-8c75-323a-ad1a-7b86103c2082 | 3.24331 | -60.78457 | 2026-03-06 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc59d8fd-f52b-3bd5-af54-34534b9f4772 | 3.25643 | -60.7408 | 2026-03-06 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 498fd7da-25c8-3ce3-8a74-43851178e933 | 4.97248 | -60.26496 | 2026-03-06 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d99ee2e4-b782-3b19-9f05-f775cae1d1ee | 3.26276 | -60.73982 | 2026-03-06 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef835795-1e62-3492-9ad7-f757929b7f44 | 3.26029 | -60.74155 | 2026-03-06 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6b0c227-b718-36fb-b3a5-174443952054 | 4.96559 | -60.26164 | 2026-03-06 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79af9245-77e9-3e50-91a6-3a93ce67e904 | 4.96952 | -60.26309 | 2026-03-06 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2dc7f73b-1971-353c-a84a-ec6ca7d9be79 | 4.96627 | -60.26639 | 2026-03-06 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de70b93e-65e2-3938-919f-c5b1c30ab8ed | 3.99984 | -60.16348 | 2026-03-06 04:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc0377f2-69d1-3c96-a2ac-521ae47021b2 | 3.99913 | -60.1587 | 2026-03-06 04:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5abce9b-0c62-3b8a-bbc8-d17d8e4aee2c | 2.22882 | -60.22585 | 2026-03-06 04:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cfc53cc-2dcf-3dad-bef2-86cd2e718cad | 3.24746 | -60.78517 | 2026-03-06 04:46:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91263380-824c-321a-9da2-c5bbcc11d7bf | 2.23485 | -60.22485 | 2026-03-06 04:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d7d8093-7174-3306-808c-1d2e45c43fa3 | 0.9367 | -59.34686 | 2026-03-06 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39a7373c-ee3b-310a-8bb7-c026397a102e | 3.24669 | -60.78007 | 2026-03-06 04:46:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48876970-7ab1-3a1b-9985-eafd8306083b | 0.93728 | -59.3506 | 2026-03-06 04:46:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3c5f545-f304-3e18-bc82-70897923d065 | -11.64956 | -55.30024 | 2026-03-06 04:48:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 692f44d7-44ed-3e3b-b064-a4ce5b4d4db8 | -19.23967 | -52.34856 | 2026-03-06 04:50:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4bbb1e6-e03b-31b5-9e02-9cab294b6808 | -19.17335 | -47.35868 | 2026-03-06 04:50:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 043bbab9-8efb-38d8-8d31-0425da793fe4 | -13.18344 | -53.30673 | 2026-03-06 04:50:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db8a0bc6-815a-38c8-a851-b8119287a3f4 | -18.97221 | -51.86412 | 2026-03-06 04:50:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58fa2a07-6812-395c-9e23-4d6ef9e2a1b6 | -19.16889 | -47.35808 | 2026-03-06 04:50:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18b76061-82aa-3608-8f90-41cd874ed20d | -20.35456 | -48.34443 | 2026-03-06 04:50:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0b0158e-980c-3c3c-b1bb-905b2e57bdc0 | -19.1434 | -50.60331 | 2026-03-06 04:50:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b8b70cd2-d5d1-3e0e-ae12-e9d8debe4ea7 | -18.97108 | -51.8629 | 2026-03-06 04:50:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d171ec35-6c73-306f-9668-987257b76e0f | -22.92259 | -48.61185 | 2026-03-06 04:53:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 876b3540-fe63-35e4-a872-13f8f3ad2940 | -21.66314 | -56.32864 | 2026-03-06 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4735fb5c-6b24-36e7-b3f1-19b89cfdc4da | -23.09122 | -52.3584 | 2026-03-06 04:53:00 | NOAA-20 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bc594450-90b8-3362-9367-0f02f9dbc3f8 | -21.32686 | -49.00001 | 2026-03-06 04:53:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c085ea1d-a30b-3cd5-bfd5-c98a489f2673 | -23.47941 | -54.17208 | 2026-03-06 04:53:00 | NOAA-20 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6a512f41-ed78-30aa-b430-28774901b40b | -21.71187 | -48.43637 | 2026-03-06 04:53:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb7be6dc-931b-3b45-8e9e-743064bdcfb5 | -21.29606 | -49.31751 | 2026-03-06 04:53:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b39fa313-ea53-3553-9c0e-e5e42bdf3573 | -20.25159 | -50.74908 | 2026-03-06 04:53:00 | NOAA-20 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe864463-f565-3b41-a9ee-987c4ecf4084 | -20.91715 | -50.52928 | 2026-03-06 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a9b0214d-5a2a-3f60-80c7-f0395fd347e7 | -20.20611 | -50.65067 | 2026-03-06 04:53:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| a41bc5c1-3187-3a00-97b6-1f89cd93cbb3 | -22.92794 | -48.60371 | 2026-03-06 04:53:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 904348a6-fa5c-3e2f-b35f-514c132aa232 | -21.19649 | -49.18805 | 2026-03-06 04:53:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9e94d3d7-eedb-3e9c-ad64-a558a2ff3e14 | -23.79108 | -53.32219 | 2026-03-06 04:53:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 712ebf34-4eaf-3c37-bd6c-e1c4a1d11b20 | -21.6665 | -56.32932 | 2026-03-06 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12ae3331-1daf-3943-a2a3-bf21b27cdaed | -21.66379 | -56.32479 | 2026-03-06 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
