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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52506eb7-17bf-3f2a-9dc5-0397601063ae | -12.77728 | -44.8754 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d2b2dec4-4452-3a9f-a65e-6647fd27fddd | -12.77589 | -44.86137 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8202db68-3120-3d4c-894b-b42ea149a46c | -11.94628 | -44.73129 | 2024-10-11 04:02:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54c4af5b-205a-3dc4-8741-ebc4f6a767ac | -11.89474 | -43.88526 | 2024-10-11 04:02:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3169cd87-be80-37ae-9da6-7a5b0cf5dbfa | -11.89406 | -43.88935 | 2024-10-11 04:02:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92a921ad-6a67-3547-9f78-ff08950c2603 | -11.78899 | -44.4935 | 2024-10-11 04:02:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33f48db9-3ae9-3943-9164-b0654c371675 | -11.78825 | -44.49788 | 2024-10-11 04:02:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0440510e-3d61-3e5f-a77b-ad3061809147 | -11.76036 | -44.48398 | 2024-10-11 04:02:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd6d86ef-56fc-3d63-8c0e-65c122920b19 | -11.75226 | -44.48707 | 2024-10-11 04:02:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f6bc6fd-47c2-348e-8c2c-707aef2c123e | -13.71039 | -44.44785 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99121337-abac-3ce2-93ed-159a326aea23 | -13.70681 | -44.44724 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 213d1fbd-1098-37dd-8fd0-5ce09e9062c7 | -13.70609 | -44.45145 | 2024-10-11 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b6337f8-241d-38c8-ac73-c450d1666d18 | -13.36978 | -44.77734 | 2024-10-11 04:02:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d68599aa-4287-3605-819f-07c95eb02ed4 | -13.36904 | -44.78168 | 2024-10-11 04:02:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59f2ace1-d7b7-34ab-99bc-fdb6555f5619 | -13.36613 | -44.77666 | 2024-10-11 04:02:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 134354a1-e9bb-307e-a8e4-975058e7f3b5 | -10.30307 | -43.41984 | 2024-10-11 04:02:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0e5971a-4cd6-350c-abbf-cf2dc2a8ad29 | -10.29952 | -43.41922 | 2024-10-11 04:02:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90fb8ee1-f6d5-39a1-babc-a911a87c2393 | -10.29884 | -43.42332 | 2024-10-11 04:02:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4f561a1-3356-31f1-b3c3-94f67c8d95d6 | -13.99327 | -48.0265 | 2024-10-11 04:02:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27757efc-d8dc-325e-8f83-7b42e360a398 | -15.57041 | -47.85638 | 2024-10-11 04:02:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5eb5df5-db51-3c48-aa1e-f0529d31d6cc | -14.06635 | -44.94445 | 2024-10-11 04:02:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cea53208-6b56-3a2c-9c13-c18e34476fcd | -14.0513 | -43.6923 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d8f91d4-dcba-37fa-8f76-dcc392bb849a | -14.04785 | -43.6917 | 2024-10-11 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43f9555d-3632-3027-b07f-fb9a1e49729d | -14.73071 | -42.29529 | 2024-10-11 04:02:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50d526df-9047-3856-95aa-67f3e71f6250 | -14.72738 | -42.29472 | 2024-10-11 04:02:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| baf87e94-c6e4-3098-bf2f-3c7029be0114 | -14.20904 | -42.75815 | 2024-10-11 04:02:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d241ad5a-7617-3450-8b21-e40aa915fcc8 | -13.9034 | -42.85066 | 2024-10-11 04:02:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e37fb1f-9516-39e1-8609-ed1ad54efd3f | -15.1207 | -43.63202 | 2024-10-11 04:02:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a247b590-4ef8-37ad-8263-6089449b3cab | -15.12007 | -43.63581 | 2024-10-11 04:02:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b7f19678-a58e-3a24-91ff-8572b783e777 | -15.11789 | -43.63158 | 2024-10-11 04:02:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4a0d9b0c-e2c0-3446-9c01-14a1d6e4cd6d | -15.11728 | -43.63142 | 2024-10-11 04:02:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd4c7edb-07e9-389a-9435-4cf0a1933acc | -12.77651 | -44.87987 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 960bcd89-ced9-3793-85d2-521208004386 | -13.36539 | -44.78101 | 2024-10-11 04:02:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6076d919-58a0-349d-9c32-1fe17a51dc38 | -12.77574 | -44.88434 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0062ec6d-15a7-30bf-88b6-f445c6d9854e | -12.77512 | -44.86583 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5ea26f79-8fb0-31d5-b1f8-0ce4ed040ca3 | -12.77497 | -44.88882 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0e307fb2-d6d5-360a-80c1-a2b5d8d23b69 | -12.13695 | -39.40361 | 2024-10-11 04:02:00 | NPP-375D | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d99bfc27-fbb9-34a0-8068-c1809038ead3 | -13.05113 | -39.9714 | 2024-10-11 04:02:00 | NPP-375D | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a8f4e76-df4d-3ee8-afa6-e71cac2b710a | -12.89771 | -41.11839 | 2024-10-11 04:02:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c731a722-1418-3ef0-b129-ae1fc4fcbc60 | -12.87614 | -41.76838 | 2024-10-11 04:02:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 58dca44b-ffb5-3256-b318-5a521331b818 | -14.65854 | -41.01526 | 2024-10-11 04:02:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d8f8e252-4fcf-3a34-9cc0-952eeb1130f7 | -14.11868 | -41.6777 | 2024-10-11 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 380c8c86-b604-3dd4-9ad8-8619b9a6ba94 | -14.0098 | -41.01324 | 2024-10-11 04:02:00 | NPP-375D | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7c8aff4b-56b6-3094-9b7f-e25b02416aa3 | -14.00924 | -41.01682 | 2024-10-11 04:02:00 | NPP-375D | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cadcea68-c790-3db4-9b06-cf97090f91b8 | -14.00591 | -41.01627 | 2024-10-11 04:02:00 | NPP-375D | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9105a2d2-ade2-3d2b-b4c4-33ebf7549d6c | -13.89763 | -41.2947 | 2024-10-11 04:02:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2aa14217-720e-3e1b-8adf-8aedfcd0f748 | -13.88716 | -41.66486 | 2024-10-11 04:02:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 272f606c-0310-3924-b9ff-c97a7d7c6473 | -13.76532 | -41.81653 | 2024-10-11 04:02:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 206363ef-2ba0-3cca-a291-d469c4a60305 | -10.79952 | -42.44828 | 2024-10-11 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f128cda-2099-383c-aa1f-668202e155b2 | -11.01577 | -42.87247 | 2024-10-11 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3bce19f1-eb63-3d61-8d07-ce214f4ec709 | -11.08792 | -42.30667 | 2024-10-11 04:02:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66a34346-dacc-3be9-b394-450f0dfbd7ce | -11.83616 | -42.82025 | 2024-10-11 04:02:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8498d6da-2ebe-3841-b506-834d2dc242af | -11.21781 | -41.60325 | 2024-10-11 04:02:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc9765e8-145c-357a-a41a-8c508b8d87b9 | -11.21448 | -41.6027 | 2024-10-11 04:02:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 38a82bc0-9d3d-3e08-9447-33fd519aec75 | -11.21391 | -41.60625 | 2024-10-11 04:02:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ef6259e-6484-3e56-af48-09ff5b2abbf4 | -11.08851 | -42.30302 | 2024-10-11 04:02:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24ab2685-5d39-3d90-a722-d7220aa47611 | -11.08513 | -42.30244 | 2024-10-11 04:02:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5dda61b-4e2b-326f-93fc-af6abc63e4fd | -11.0164 | -42.86866 | 2024-10-11 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba2fff61-8c38-378b-b461-811a58399cc0 | -11.01384 | -42.87303 | 2024-10-11 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 79c8bc32-4f28-39cd-9363-d41500ec09bc | -10.83766 | -42.23547 | 2024-10-11 04:02:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6798eb33-0c32-3a27-b70c-fa41ccbfb18d | -10.84367 | -42.8601 | 2024-10-11 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bec7b17a-d166-3639-9d86-7a1c32364e9f | -13.02579 | -42.66248 | 2024-10-11 04:02:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 677396df-7b98-33fb-8e24-5de14ad57271 | -13.02241 | -42.6619 | 2024-10-11 04:02:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19b86155-1cfd-3268-9ac7-420f02d6d1de | -12.59305 | -42.41894 | 2024-10-11 04:02:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b03eac2-a2b3-3554-89d4-ec171f0c3437 | -12.43151 | -41.79747 | 2024-10-11 04:02:00 | NPP-375D | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3973da9-55a8-3d36-b9fc-5a4ac6aee2a9 | -10.44853 | -44.15693 | 2024-10-11 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb09c1e5-455a-3b18-a538-6fb5cb5f76ab | -11.11155 | -43.33769 | 2024-10-11 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 864478de-5d02-3dae-81b3-7657c56013e1 | -11.49393 | -43.22736 | 2024-10-11 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 79ce11ac-b503-3a55-a741-e4b9dd638376 | -11.48982 | -43.23065 | 2024-10-11 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c13b28e3-2782-3465-bbec-2a9bb7a82f9c | -11.526 | -43.99079 | 2024-10-11 04:02:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85edd423-1f5d-3b96-93f0-653c68c01739 | -11.5253 | -43.99497 | 2024-10-11 04:02:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bfddfc3-5e4b-3036-916e-a62fdbb65ce9 | -11.5217 | -43.99435 | 2024-10-11 04:02:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32ae0e2b-993f-318f-a3e8-ddb79f7879f9 | -10.85676 | -44.44233 | 2024-10-11 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c024b5e-40b7-3dee-aa69-9e6db1a65a6f | -11.49266 | -43.23513 | 2024-10-11 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9f1f42d5-6eb5-38b7-85d6-6c75d9109cca | -11.10805 | -43.33709 | 2024-10-11 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dce80a0e-2b06-3ac5-aaa8-636f93f0a073 | -12.77435 | -44.87029 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 58e21e04-6e65-353a-a47b-8e70ba4c13ec | -12.77359 | -44.87474 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 6058b25e-9e23-3c0a-8118-799f368fc3f1 | -12.77282 | -44.87921 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 11811b33-1aeb-3c05-8b4d-6b499bd01ce3 | -12.43091 | -43.74363 | 2024-10-11 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d8a06a0-f6c2-37b8-9e1e-2b1aee078166 | -12.77219 | -44.86072 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f85c4e23-6de2-3c7c-bb3f-5dd021bc9c28 | -12.77205 | -44.88367 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fd9fc3d1-cc4f-38a0-989b-2cdb17992d9e | -12.77143 | -44.86517 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d39a8387-4f94-36fa-94e9-601618d7ed69 | -12.77066 | -44.86963 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b7090fc6-9980-3c04-a078-4fdbc6335fec | -12.76989 | -44.87408 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e39a1f9c-2484-3c67-9b11-3e1181affab8 | -12.76912 | -44.87854 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 87df0546-9da1-3f3a-b156-172f2ef3a062 | -12.76696 | -44.86897 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6541a54a-e5dc-36b4-a86b-6f7a6c10d7ef | -12.65709 | -44.24494 | 2024-10-11 04:02:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ea5ce0f-ce21-3532-916d-1c385bd3119d | -12.58476 | -43.36547 | 2024-10-11 04:02:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc3aab9d-5d57-3b50-8113-66b8be062104 | -12.5813 | -43.36488 | 2024-10-11 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ddd39da-042a-3a4f-a299-ec77afbe52d8 | -12.58065 | -43.36874 | 2024-10-11 04:02:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03fa745d-22d8-3ed0-b6cf-e0fea721cfd9 | -12.43443 | -43.74424 | 2024-10-11 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5c0e861-dafc-3325-a8b2-1526d2b95f9c | -12.37599 | -44.11393 | 2024-10-11 04:02:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfa8b87e-ed57-36f1-b3e2-4790c24bf9cf | -12.35395 | -43.75184 | 2024-10-11 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a36055b-1827-3d2e-89a8-3774ce0cdbd5 | -12.35329 | -43.75581 | 2024-10-11 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2349839e-48b5-367f-ab6c-4eec502439f2 | -12.35044 | -43.75116 | 2024-10-11 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 713691b5-724c-3a48-bafd-d2223d973d61 | -12.34978 | -43.7551 | 2024-10-11 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 6d795a64-61a5-3e8a-9cb7-1ce277f96b82 | -14.71805 | -44.8087 | 2024-10-11 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c7a9e3c-c953-344b-97b3-18ece4e81d82 | -14.36529 | -44.66003 | 2024-10-11 04:02:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1ac8024d-5696-3574-a27d-2823645c857e | -14.19009 | -44.37091 | 2024-10-11 04:02:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adcdb63f-4b50-385f-9d97-b1bc68cfa956 | -14.18655 | -44.37025 | 2024-10-11 04:02:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README44.md)
