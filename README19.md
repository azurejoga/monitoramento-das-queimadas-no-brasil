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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19bd9d24-a13d-3841-b130-b3c9ddc19ec1 | -15.52362 | -48.40104 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d8257b2-54f5-3d02-b08b-6c28377dab98 | -13.83786 | -46.23489 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 605f2f5f-263b-3ccc-b369-b5f7e2b84e7e | -11.8387 | -46.76399 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77691ad4-abdf-35ed-ac2a-2014f4518346 | -12.89046 | -47.98607 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 153a3b2e-a993-316c-aacb-ca324cd2b71b | -15.21597 | -44.0373 | 2025-09-09 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 377bc971-9b40-3678-aaef-8b08d6ca5ec2 | -13.01957 | -48.03502 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70922ca7-3ed7-37b4-abfa-4d85ab6eaaa0 | -15.5232 | -48.39362 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f19cc0ec-9b26-3dc6-9077-b61917022299 | -17.48861 | -43.33576 | 2025-09-09 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a8c8f96-82f0-3edd-a77e-d74265c2b58a | -13.48027 | -43.50618 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 912ecc4e-e26b-3246-b49c-5d8e76ca5dba | -14.24381 | -44.95366 | 2025-09-09 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 220a0ed7-c250-3a1e-ab4f-12506e50fe46 | -11.82209 | -46.75868 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b214d72-53a6-3507-bed1-3e2b2455ffb2 | -18.11952 | -45.32391 | 2025-09-09 03:45:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 598013ae-d0d7-3d38-81a0-dbe4d234c110 | -14.28627 | -45.01906 | 2025-09-09 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5802ba0-ba48-3a29-abba-f8402f0e82e4 | -15.528 | -48.37109 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73a77faf-1104-3ed6-939c-eba4085058b2 | -18.76508 | -47.09729 | 2025-09-09 03:45:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25455841-d943-385e-9ebc-25786ad81b02 | -13.03361 | -48.02743 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a4930c6-d397-35da-8ca0-aa7e5d90bd23 | -15.52424 | -48.36834 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 154b54d2-d528-3ea5-803c-86e4b7c4dc86 | -11.45293 | -49.27684 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9afade38-bf32-3e2e-b69b-01cbc2b2911e | -16.95198 | -45.81626 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d83b7f6-ad73-33a1-a6c2-3006540a3ebf | -17.34353 | -43.59239 | 2025-09-09 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d3d7238-e717-32ba-936a-117470068499 | -13.72585 | -46.88674 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78cb0a66-88cd-3235-8965-f59cbb2b4b59 | -14.34684 | -47.30957 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5938f3f5-d6e8-3fdb-8548-3f8a5a9738d3 | -14.79163 | -48.18839 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 384a8386-d761-365b-8a60-eec594aa0a6b | -13.2865 | -43.73795 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7ae5e43-d376-3420-a1dc-bf75d7b132f5 | -17.14796 | -44.44735 | 2025-09-09 03:45:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fc8a6dc-eec4-3c92-9704-22906d41dfc1 | -17.28535 | -46.70199 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b6eeb20-c49b-3ed2-8638-e72cce2cf54e | -11.29849 | -46.49228 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da5e7e18-7b1d-39c3-b9fc-822749ce3878 | -12.87195 | -47.97503 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ac39d77-e488-332d-bd42-188506a19756 | -15.52868 | -48.1707 | 2025-09-09 03:45:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 663c9748-fb94-3416-8160-ccf55379e658 | -13.93826 | -48.23685 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5678be14-1134-3b0a-a2c2-901fe75a4bb5 | -13.82734 | -46.23258 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3502c11b-c92c-3784-89c8-eea76e3402b6 | -14.33713 | -47.31171 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f42b130-de7c-30fc-8516-813972576fe7 | -14.34738 | -47.30692 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 647c7373-ac00-39c7-91fa-f3abcf9f7c44 | -14.20883 | -42.07835 | 2025-09-09 03:45:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1673d605-2d98-3934-b692-862441405cbb | -16.89037 | -45.78241 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8232a22c-4ee3-3979-838f-244712d7262f | -11.82765 | -46.76028 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 126fc033-8e10-37bf-a7c2-16525c2c65f1 | -11.46195 | -49.26627 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e718c83c-e76a-371e-a8b2-fb098182fb71 | -11.29924 | -46.48841 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a373c99-ca70-3cee-9967-615aa2123796 | -12.85232 | -47.97956 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1183efcd-0e21-31cf-baf7-da0d5bc5368f | -16.28251 | -45.68504 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99586bf9-6029-3af0-ba94-e1267b49dbfc | -13.79001 | -46.28205 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1700e438-420a-3ffe-a626-0dd0d4123f49 | -16.43164 | -49.29308 | 2025-09-09 03:45:00 | NOAA-20 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71be9ab2-35c5-3d15-8c06-14cff009d602 | -14.32762 | -47.33022 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9a190b2b-7eaa-3a65-8ff1-a99e72612f1f | -13.74648 | -46.89528 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 600073c0-8412-3488-8e82-4f036f26e872 | -17.29878 | -46.71431 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2677d05b-3c2f-34f3-ad02-8d88bd08c8f5 | -14.3362 | -47.30457 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bf528f8-4e14-3798-a2a8-e2fb292b6f91 | -13.94977 | -48.24145 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 634d967d-435b-33e4-a48f-e0d9f805e045 | -14.60253 | -43.927 | 2025-09-09 03:45:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5e302fb-aa14-3345-91a9-b3d529808d78 | -14.32843 | -47.32616 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 33fc7633-db36-3fe1-8143-d7be13d40d94 | -15.52197 | -48.174 | 2025-09-09 03:45:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfbae2f6-c584-3e92-a43c-c0fbf05639b5 | -19.15271 | -41.82953 | 2025-09-09 03:45:00 | NOAA-20 | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ddff1c5e-0ba3-34d3-ba79-160991ce61ae | -18.0102 | -47.1139 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf1c2712-3e24-3994-8c98-83c2b7c5ac53 | -14.79502 | -48.19292 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5920eaa-a674-318b-af6b-0b571aa52ea8 | -16.9004 | -45.82138 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d7bc16a-f611-35d6-899f-c046df8e59c9 | -16.28556 | -45.68092 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8a43501-8ad7-3408-b900-c64b01141348 | -15.11349 | -48.11325 | 2025-09-09 03:45:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b93ba83-e182-374a-a90c-f4d9178e5f90 | -16.92844 | -45.85812 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2528281-f63a-3bad-9e7a-2071502aee09 | -12.53413 | -45.26651 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95c5776f-75f2-358f-9bfc-293dec9c3d07 | -11.34176 | -46.57123 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5619e93d-b3f8-3193-81b6-963fe77d8c07 | -15.53015 | -48.3897 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7b863e2-2f45-34ca-94a6-2a54f5f6bd33 | -16.28928 | -45.68765 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ed94956-2a47-31c4-a995-50e0a83595ff | -13.04311 | -47.1553 | 2025-09-09 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3fbf7dd-8bec-3192-8b5a-a68a59bf8708 | -14.53549 | -48.7544 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63dff1e9-8d45-387c-a1ca-bd775171ed3b | -15.83128 | -48.94785 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b47413f-6888-373e-8a7b-ade4f1e79f19 | -13.79431 | -46.26054 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df9b1110-42f9-327d-b5ff-b480b24a546a | -11.46074 | -49.27227 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7de0877c-06f8-3076-8113-05ce2b226915 | -15.53501 | -48.39565 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79555166-6d73-34f7-9990-6b4c9043485b | -11.33955 | -46.56567 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0faab997-bfe8-359d-ba40-293fcb27fd44 | -15.5222 | -48.39832 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d2f24ee-fab4-39d7-ab19-04ced53f0075 | -13.02062 | -48.02991 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4a9a8ad-0bfa-3ba2-8672-300b4c706774 | -13.79296 | -46.26726 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da17511c-fac1-3215-bd8d-040c52b60c88 | -12.14985 | -49.08028 | 2025-09-09 03:45:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efb6f0fb-4664-3247-9db4-9826fcad77c3 | -11.34294 | -46.57817 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11165d0a-8238-3473-8f40-484361c85050 | -15.82861 | -48.96012 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40d1e8f8-68e1-3828-a98c-376068c3512a | -13.8248 | -43.86557 | 2025-09-09 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6bf0586-6421-34d4-9313-14c2296b76c8 | -12.51886 | -45.2915 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfe4e06c-7caa-3b29-a9f0-6f03e3f00236 | -17.72831 | -44.49495 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2c459726-4d2b-38d6-a37c-216be9b9d58e | -17.27623 | -46.74606 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16e54b12-053d-3d93-a74e-42ce3e012d29 | -13.95557 | -48.2435 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06949440-df14-31d9-a227-69556de74d08 | -17.29813 | -46.71745 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21ae2d63-8284-317a-b087-76329e02ad84 | -14.60787 | -43.9233 | 2025-09-09 03:45:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45e6c45e-e05b-3e33-8eef-6a3722b38b92 | -15.53012 | -48.36941 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a491a346-4df1-3e5f-b521-d31793e8936c | -17.71907 | -44.47356 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cf6d3e2-5cda-3b3d-9312-7001baa8b58a | -16.42458 | -49.29624 | 2025-09-09 03:45:00 | NOAA-20 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 895bbae3-5c32-3ead-9221-a8d540889ad0 | -14.33138 | -47.31133 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60cceccc-b3a1-3af3-9e3e-97f8615d3778 | -15.5397 | -48.37352 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e0899d8-4412-3069-a0cc-668d25074ef0 | -13.80634 | -46.28309 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4b724fe-9f81-3974-b04b-28b3b12d7e86 | -13.27814 | -43.7529 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19453db0-e96e-3e51-bbac-d14223a823b9 | -17.76905 | -40.19394 | 2025-09-09 03:45:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 268f80c2-f117-3d83-9572-ad51a020b2d0 | -13.944 | -48.2392 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef26035f-ac89-3b31-a0bf-90eef2837221 | -11.34103 | -46.5751 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6a5d931-e223-3bab-8314-58ddd1959c7a | -13.83261 | -46.2337 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a70a6a4a-465d-3eb4-b8eb-aa1c43d99fa3 | -15.52884 | -48.36712 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 842918f5-de16-3fe3-a94b-ed4e55d9aacb | -19.47931 | -43.90016 | 2025-09-09 03:45:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca109a16-9208-3c8e-8a68-02dcb9fe8f6c | -13.65735 | -46.96999 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 345f6344-d5b2-3619-bc3a-c86ce46061a0 | -13.28523 | -43.73967 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8de1fe8d-50a9-3fa0-9ebf-46895f041707 | -16.88991 | -45.75908 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bc58628-79ff-32c4-98da-91a88f040aae | -12.409 | -40.9254 | 2025-09-09 03:45:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e79cae9c-d9c3-3a3f-ab9c-2395b5c27fa2 | -12.53021 | -45.25943 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86cffca1-eec7-3113-8f46-11c999f5ef7c | -12.5692 | -43.78307 | 2025-09-09 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
