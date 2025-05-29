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
| 1a135da7-77a6-378c-9a86-c9b41a1cf6a9 | -8.6725 | -48.28759 | 2025-05-29 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a97d2c65-95a2-37b8-aa7e-3acbc79206a8 | -9.20613 | -49.47934 | 2025-05-29 03:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| da20202d-52f8-3116-8b31-6ca8fc7abe5a | -6.23878 | -43.37318 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e256b2d1-2eee-3bd3-abe7-799c85ca59dd | -10.73806 | -49.2905 | 2025-05-29 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47c3923a-979e-3d17-9f0b-ac51a565ea9a | -10.65656 | -44.49235 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0ba67d80-59b5-3fe6-afe3-efc68a70d027 | -11.58181 | -37.6565 | 2025-05-29 03:51:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e172b12c-99c2-3760-8d7d-bffcd3dcb2b6 | -13.66123 | -45.42251 | 2025-05-29 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97e4e4d9-5a17-33a1-a76d-ac4d4a18248e | -13.08794 | -45.29106 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 167d4049-4efd-3754-8d0d-7af10bfaf406 | -11.82179 | -44.26802 | 2025-05-29 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1c4eab4-482b-396f-8d1f-fb07480204b1 | -11.56942 | -47.62602 | 2025-05-29 03:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12178301-a20c-37b8-9af2-c030ddca9460 | -13.0834 | -45.29017 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7078b4f6-39a7-3aee-b903-38bce0a32630 | -14.66744 | -45.08713 | 2025-05-29 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7953095-2cbf-3901-bc8c-8b90c2f653cc | -10.95618 | -48.15628 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8afb8517-a818-374d-9b51-b6b59b90dbe3 | -13.68591 | -47.68722 | 2025-05-29 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 311de3f5-e4f4-3729-921b-fcbaf0ac0375 | -10.65127 | -44.49603 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 305e5e4a-b935-32ea-8841-3fc06e5d7381 | -18.18344 | -42.63546 | 2025-05-29 03:51:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74de2829-e5c9-35aa-832c-768bbb75e486 | -13.08965 | -45.28168 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d882295-8e3d-31a7-93bb-f08c09be5b81 | -13.66036 | -45.42719 | 2025-05-29 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0d1e5e2-d9f1-3906-a727-2431ede6b6b5 | -10.95204 | -48.14725 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03c1ac36-8f26-3f98-a77b-0ef4fa22243d | -11.57486 | -47.62708 | 2025-05-29 03:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 057be625-a3e1-38be-be58-0721d3ef2106 | -12.30496 | -47.26967 | 2025-05-29 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11c6bf64-7d24-3920-ae58-b90ff1ea0ecf | -11.97564 | -52.4612 | 2025-05-29 03:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 711febec-b0c8-3979-94c2-af76775dd92b | -10.67516 | -44.41252 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92827768-39a2-344c-b6fc-b040de643750 | -10.66627 | -44.41059 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ad498a9-f096-3c8a-a74b-cd899a1ed2b7 | -15.07606 | -43.37432 | 2025-05-29 03:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b132da8-f970-3c53-9d93-2f1d759ba170 | -12.26027 | -44.60552 | 2025-05-29 03:51:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7be76854-7fcd-3e00-a1d3-8e7935e6f56c | -14.66823 | -45.08297 | 2025-05-29 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fbb1abb-9cff-3b60-b1e9-8a316f20810a | -13.07972 | -45.2846 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 885a78a7-2604-397f-8c8e-460b4d62dce1 | -12.3822 | -49.97243 | 2025-05-29 03:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5a5f47a-b7c5-37e6-acd0-d959cfe54a9a | -10.66994 | -44.41601 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59ae8132-6639-3b48-8dbf-f3d5a80b7bfd | -18.17985 | -42.6348 | 2025-05-29 03:51:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fdbb8718-7755-3a64-8717-db36ef885cc9 | -10.73197 | -49.28914 | 2025-05-29 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3edbf683-757c-3a3c-93de-02e447ae8b15 | -10.67315 | -44.41 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d09b867c-2a7b-35e9-a06e-1454bfbfab62 | -16.68007 | -43.88248 | 2025-05-29 03:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46dca738-2e03-3278-80b2-5aa470d5f77b | -10.73097 | -49.29411 | 2025-05-29 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3276e10-7d56-3cac-9535-589b8c4bfda2 | -10.73251 | -49.29335 | 2025-05-29 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cce0995e-8a37-3818-a88c-fac9d12d1dfa | -10.66181 | -44.40974 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4c031d9-d4f3-384e-9544-15bbc81c14b0 | -12.38592 | -49.97515 | 2025-05-29 03:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19cb669f-178d-363f-bf09-b6ab838047d8 | -11.79933 | -44.26823 | 2025-05-29 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b47d359-d947-3b1a-a8e9-142935b9dd0a | -10.65759 | -44.49508 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd80da5d-b8af-3394-95ac-3a3bc4aee4c8 | -17.32793 | -43.61281 | 2025-05-29 03:51:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b3b9f8a-b9a7-31c8-836e-b2b289bd6c57 | -12.30986 | -47.26809 | 2025-05-29 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7881e2a5-52d7-30fc-840d-ed977b93e782 | -18.0409 | -39.92556 | 2025-05-29 03:51:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd9c70d9-517a-3eba-b981-5d6e25f3e14e | -13.08426 | -45.28548 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f25211f-698b-3e16-a69a-d49f31dcf600 | -15.80402 | -43.56935 | 2025-05-29 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa6ff308-6a26-3c0f-a591-71fb34737050 | -10.6531 | -44.49425 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 70d3560f-49cc-3e3d-bf65-d6a42d3dcf0e | -11.28673 | -46.44268 | 2025-05-29 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d74d9c2c-499a-3685-8c88-cdbe5b46d94b | -10.47105 | -47.94659 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 872bd267-9f7f-371a-a187-b809f9b5a108 | -11.80443 | -44.26483 | 2025-05-29 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1928860e-1a0f-3bbd-9a54-f9152a6aa078 | -10.67073 | -44.41146 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aecaedf3-55f0-3f1a-bfad-5ba1de9814f3 | -15.48005 | -41.89756 | 2025-05-29 03:51:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5b9d4633-7a97-3b80-8d8d-9073f7b05ee7 | -14.67179 | -45.08802 | 2025-05-29 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f4673e4-70e3-3f85-9f0d-1022628ca8c3 | -10.66342 | -44.41271 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63c0d74a-a81f-328e-a5d6-05c1fe84f1a8 | -11.81745 | -44.26722 | 2025-05-29 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| f5431b13-0d3c-3bcd-93dd-1ee57813c006 | -11.2828 | -46.43577 | 2025-05-29 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b05e760a-4e55-303d-a325-cdbfb3aa8fcf | -10.95644 | -48.15018 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce6ba39b-d88f-37c4-b140-b241e5858a8a | -12.38843 | -49.97362 | 2025-05-29 03:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d7095a0-9625-3032-b75a-fa186b52edf5 | -10.7188 | -49.54879 | 2025-05-29 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f90e49a-a33c-39dd-9203-e12628bf19e7 | -10.63732 | -48.80978 | 2025-05-29 03:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d0d5b2d-e539-331e-aae8-a28a01fcad2f | -11.82103 | -44.27222 | 2025-05-29 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72d5dc6e-d952-3970-a3a9-227e5dccc4eb | -14.67099 | -45.09227 | 2025-05-29 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 784e4a53-45ac-3c59-aaca-8865dd651a1d | -14.52957 | -48.33618 | 2025-05-29 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc8f3406-d82a-3047-b889-a8f646b0c0a5 | -12.38696 | -49.97015 | 2025-05-29 03:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83b836ef-869f-3c28-8ff4-b513c0798a59 | -13.65823 | -41.61984 | 2025-05-29 03:51:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 72989c1f-104a-3fa9-9c4b-69d0f5fc92f7 | -10.73156 | -49.29827 | 2025-05-29 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f41f4d89-bcb7-3ab1-a5d6-592fb5283cd8 | -10.4703 | -47.95046 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8af8fb2b-db8b-3b70-9c43-3b481311dbc4 | -15.69862 | -42.25537 | 2025-05-29 03:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dc9c06e-51f8-31de-a1c8-1e79d5ea81aa | -13.71183 | -45.25101 | 2025-05-29 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b63705f-acd6-351b-9070-70cef7d6c479 | -13.08511 | -45.2808 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cca6a8b-2bd1-3eea-af7c-fd08c623fc55 | -12.32025 | -49.99059 | 2025-05-29 03:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b708054a-23c4-315d-a71c-d5a3f1748dcb | -12.86301 | -38.36776 | 2025-05-29 03:51:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d55d9459-543a-3780-94a2-a2e804d551bb | -11.78182 | -47.32086 | 2025-05-29 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03947618-f6d2-33d8-b3ea-4aeda281c58b | -10.95051 | -48.15506 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 269a1e1a-f474-377b-9bca-83f16992ef75 | -14.77582 | -42.47087 | 2025-05-29 03:51:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5e893ff2-35ca-31ed-b3bf-8e342fc52b66 | -10.645 | -48.80218 | 2025-05-29 03:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bc44b15e-9899-32f1-9d49-a4c2b3213f63 | -14.06866 | -41.84155 | 2025-05-29 03:51:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 342cee26-1db6-3ae8-90b7-aed0f5f1bd0e | -10.52894 | -47.58661 | 2025-05-29 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9db6004-b226-3e96-9093-c5116725e8d9 | -10.73862 | -49.29467 | 2025-05-29 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 54c71377-a106-393f-8a6f-bb359c955e2d | -12.30401 | -47.27017 | 2025-05-29 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1edaa477-a5f2-36ff-adb8-cd8e39bbc3e2 | -15.80376 | -43.57114 | 2025-05-29 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5582470-6227-360a-b097-91d37d6d9df3 | -12.30336 | -47.27347 | 2025-05-29 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cad7c645-1ab1-31cb-91df-43f6e7486bfd | -10.95571 | -48.15406 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88a9056b-f594-3005-9b99-a4bd7d33b5ad | -13.08058 | -45.27991 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22db5019-5db8-3c6f-920f-e18295e15256 | -14.53352 | -48.34455 | 2025-05-29 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05af7291-07b3-30cd-a7e2-8fb00d9150f4 | -11.92325 | -44.556 | 2025-05-29 03:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09d1209f-bd14-3448-9ec9-68debd02d15d | -13.66576 | -45.4234 | 2025-05-29 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3cf6d87-acca-377b-8d94-02ab916b8963 | -14.12052 | -44.79707 | 2025-05-29 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b31bb651-33e7-3140-8262-0a6b640437e9 | -11.28729 | -46.43975 | 2025-05-29 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4a03e82-8f81-30a4-904f-0a7e4d562f0b | -13.67029 | -45.4243 | 2025-05-29 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cf1b11c-4d8e-332b-afe3-703f9a39d83d | -10.6382 | -48.80534 | 2025-05-29 03:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ac3d175-3fe5-34a0-adc9-6e8f7dc02e49 | -13.08879 | -45.28637 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7722f019-eeec-3d1a-8c98-bf89fffb2fc1 | -12.30464 | -47.26693 | 2025-05-29 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5fd25a3-adad-3b67-9bb5-5ef6ffdfc306 | -12.38943 | -49.96865 | 2025-05-29 03:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e61cbef-c7e6-3c34-900e-72faa45731d7 | -10.95497 | -48.15796 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf2ac666-6835-3258-bce5-8f40f7497a35 | -10.95078 | -48.1489 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df3b59c1-9969-3cd0-b364-cf90e43204b6 | -11.77587 | -47.32315 | 2025-05-29 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a559ac18-e81c-321b-96be-12c85f30d47e | -12.32646 | -49.99188 | 2025-05-29 03:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f751bbd6-b081-333c-846f-425f424279b8 | -14.66664 | -45.0914 | 2025-05-29 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d1cc10a-0458-3d61-a540-1dbbfddfb6b5 | -14.52415 | -48.33518 | 2025-05-29 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21dd1739-934f-3b61-9ba6-f97c9ad60c4c | -11.28785 | -46.43679 | 2025-05-29 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README7.md)
