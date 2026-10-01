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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31fd5d3e-7899-3ba0-8fe8-fcf3eeca820f | -16.18724 | -42.88184 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b08eff79-c6f3-3956-8bb4-0c043535a4b8 | -15.77674 | -46.03073 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3a14f38-d6b2-311f-b0f4-cfe6db1a0a4e | -16.18954 | -42.87816 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e73735fe-7130-3292-9447-41a177d4e5bd | -16.13726 | -43.74645 | 2026-10-01 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27352a55-e9d2-3eeb-a08b-30c8c6e8290e | -15.8544 | -41.70535 | 2026-10-01 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c04a64c8-9ed3-3f35-b2e4-b64cba6fa42b | -14.49507 | -48.30488 | 2026-10-01 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c6290a0a-8acc-308d-9bcc-ba14fb10919c | -22.14079 | -46.6729 | 2026-10-01 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5b1b3045-4eee-3d8f-a6d3-f28674a4c2fb | -18.06505 | -44.52672 | 2026-10-01 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e1564d53-5f1e-393c-a4d4-0ac5cf6a3887 | -15.85567 | -41.70888 | 2026-10-01 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 87afe1b8-e398-3c94-9a3b-742cb8691df2 | -16.15471 | -42.86739 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5059569-6e8c-3ec3-8b39-b2ca34a3854f | -18.2278 | -42.74784 | 2026-10-01 03:40:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d5e4a450-94a2-32de-bee5-3a11cb13e7a8 | -15.98339 | -41.9337 | 2026-10-01 03:40:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 428902ed-36e2-39bb-b339-b6b03c0f991b | -15.77673 | -46.03092 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b4d62ca7-631d-3838-b017-ae843e21c6e3 | -15.22926 | -46.14008 | 2026-10-01 03:40:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d741d45a-16ca-3f74-a0ee-255d3a12852b | -15.98683 | -41.93856 | 2026-10-01 03:40:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a59c82c3-737d-305b-9e66-c97e560839a7 | -17.9184 | -45.04131 | 2026-10-01 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59b766b8-6a6b-3170-a3d3-3076900e8e99 | -17.95798 | -39.70567 | 2026-10-01 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2cf1b2f3-dfe4-3be4-8f98-3a5c5e73bba5 | -18.07092 | -44.52229 | 2026-10-01 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8975bf1c-d969-3a0c-b685-4bf07f364575 | -18.0488 | -51.14357 | 2026-10-01 03:40:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c98576c4-3519-3cb0-a809-00e555ca59b5 | -16.43056 | -47.1909 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbe607ac-743b-3e0e-b427-67ac5fb4f6f0 | -16.42562 | -47.18555 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f630a3bb-6881-3807-bf34-1e88d39c64e3 | -18.09734 | -44.4157 | 2026-10-01 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbd45e71-2cfe-3c25-b216-ebcf914e1b15 | -15.64874 | -44.71402 | 2026-10-01 03:40:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f70c395d-7f76-3dad-98d9-b65ffa296449 | -18.58219 | -40.12516 | 2026-10-01 03:40:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb9833c3-f2e8-32a7-be6e-08035db86bb6 | -15.92095 | -43.52599 | 2026-10-01 03:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da33449c-4766-3ac7-a467-8ca0617c73bf | -21.71729 | -47.13803 | 2026-10-01 03:40:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee5dbe16-7cd6-3c96-9be9-3fe827670729 | -20.18509 | -50.89889 | 2026-10-01 03:40:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d5e8b53e-e61a-357b-9e5b-10d1e583107b | -16.43145 | -47.18676 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73f2997c-b8bf-35be-9ada-ff012ee39faa | -15.63597 | -43.23123 | 2026-10-01 03:40:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 03d582e9-0034-379f-a0d0-06315d533933 | -20.53708 | -45.76264 | 2026-10-01 03:40:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc16aac8-d42c-3042-a3ab-118c6e61f030 | -19.11213 | -41.49654 | 2026-10-01 03:40:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 95ac762f-10cc-3a7e-b351-f9327be2b885 | -15.64307 | -44.71605 | 2026-10-01 03:40:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6f1ed05-da7f-3050-8700-8677b91f74de | -16.11749 | -42.22048 | 2026-10-01 03:40:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 57d917b4-edf8-353b-b492-cc4ec3c63068 | -16.0219 | -45.13219 | 2026-10-01 03:40:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c89003a-e30a-3001-8952-b26bf6ee1faa | -19.03768 | -45.66468 | 2026-10-01 03:40:00 | NOAA-21 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfb02e9e-96e9-3eb1-ac69-8fc0a5564978 | -18.06725 | -44.51586 | 2026-10-01 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da073d66-3782-35d3-a341-faf388f6ed3d | -20.90349 | -47.41277 | 2026-10-01 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91626353-e325-3adf-a6ea-8fcefd52d536 | -15.9599 | -45.97495 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11d1be6a-4e23-3f66-81fe-528249d68b5c | -20.18727 | -47.40371 | 2026-10-01 03:40:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9db89074-51e7-38e9-b7e4-99e707dfdb19 | -16.99926 | -45.47057 | 2026-10-01 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94141575-e197-3309-a9b5-564477e7e8dd | -16.15031 | -42.86623 | 2026-10-01 03:40:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51496e87-6bc9-3672-b921-aee8566efc0b | -15.44676 | -45.68668 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 433cea9f-d9d1-313b-88b1-059450d8b0e7 | -17.46895 | -43.56376 | 2026-10-01 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 73252290-71d4-3676-b6df-dcd42769765d | -17.08264 | -46.82322 | 2026-10-01 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43a1dcb0-a795-328f-83c6-983b8e937df7 | -16.41949 | -47.19033 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34a04056-f984-3995-93a0-2d6481d4953b | -16.13623 | -43.74395 | 2026-10-01 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3680a329-1ed4-316d-8182-f701109901c2 | -17.31024 | -41.839 | 2026-10-01 03:40:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| db947420-d396-3f07-9895-b8d16e5b5e1c | -15.77748 | -46.02718 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f203f6c4-b25f-3340-be95-5b054704f846 | -16.13378 | -43.73932 | 2026-10-01 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 754c7510-2b06-3ab5-a0ab-7826793e0513 | -18.22705 | -42.75182 | 2026-10-01 03:40:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f55e2cd6-c4dd-3d0f-9aec-3e7156b33b3e | -19.23495 | -42.94211 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| dfc0139f-0971-36ce-b96b-4fce80a4b9bb | -14.48849 | -48.30418 | 2026-10-01 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 99e20d08-a8d9-3a9e-b466-1b5d876992ae | -21.06044 | -47.03966 | 2026-10-01 03:40:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cf3cf04-396b-39a2-b334-bbc3f7f33216 | -18.06983 | -44.52768 | 2026-10-01 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8798cf53-5547-35fe-bd6d-c975e1dece8c | -17.65059 | -39.66379 | 2026-10-01 03:40:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 56eee122-1a5c-39a8-9479-2d9189f68787 | -16.43234 | -47.18259 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12a00061-b37a-3678-89e0-9b264ddf369b | -16.42472 | -47.18978 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb4a9683-544a-33c4-b883-c573c42b882d | -16.42038 | -47.18604 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 717ad960-a313-30ca-a99f-30ae1dc34745 | -16.43324 | -47.17838 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64b60b37-6765-393e-86a2-710bb1068501 | -15.85496 | -41.71272 | 2026-10-01 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cf228640-f3fa-3c18-bcf9-32a68b395e9a | -20.18743 | -47.40272 | 2026-10-01 03:40:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 993f2ba5-fe3a-372f-8f18-9e5055b60553 | -16.41888 | -47.18859 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2e44bbe4-0708-3a4a-8ca8-366197a7255c | -16.67463 | -41.85069 | 2026-10-01 03:40:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 523be327-08f4-3faf-b41f-83ea24064624 | -19.4304 | -40.35427 | 2026-10-01 03:40:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c8d01c59-d640-3b8f-bf62-4444d5ad4b06 | -16.54512 | -41.79934 | 2026-10-01 03:40:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61acad8d-1624-3fbd-8446-4f5cbdf32715 | -16.4262 | -47.18729 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 70488c5f-13c5-35a4-9cb1-b9e7d9a7a6a3 | -15.77752 | -46.027 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77759e40-5ccb-3937-9eb6-4ed0cf8a5957 | -17.91354 | -45.03987 | 2026-10-01 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e82c7da3-b9ba-31d0-95b8-58cc9170f8cd | -19.22964 | -42.94954 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 23eadf6d-03d1-3d8c-ad44-11e73ceea451 | -17.49953 | -39.38345 | 2026-10-01 03:40:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 45cbe4d0-8027-3afc-91b0-c0e7d4969ccb | -18.0985 | -44.40994 | 2026-10-01 03:40:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2e9afbe-9dfa-3838-941f-ee047c0b8e29 | -20.54199 | -45.76376 | 2026-10-01 03:40:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc5efccd-4f67-3d0e-a69f-bbf731f7bbd9 | -18.27474 | -42.18933 | 2026-10-01 03:40:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66946323-2e9d-39da-89e2-f0d92c20ba78 | -16.02125 | -45.13543 | 2026-10-01 03:40:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc8a7787-947b-3c45-85c3-4cc6701a8a4f | -18.54182 | -42.30844 | 2026-10-01 03:40:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5e3021eb-83fa-3fac-bacd-3291ea3183b3 | -21.71653 | -47.14153 | 2026-10-01 03:40:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6acf7cb0-8828-366c-bd9c-84b5036aa57d | -16.16003 | -42.86356 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 779afbef-32b9-3bdd-a6bc-4406ecddb7dd | -15.85785 | -41.71003 | 2026-10-01 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4fe643e-fa8b-3e4a-a8c8-8f05b16b8367 | -21.49657 | -46.61588 | 2026-10-01 03:40:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a7896cc0-9849-309c-a9bc-37d089bf58b1 | -15.22814 | -46.13657 | 2026-10-01 03:40:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5020613-e12b-34a2-aa9a-3a484a4a780f | -15.65379 | -44.71508 | 2026-10-01 03:40:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95451e78-0bd0-31e2-a327-8c4c0d44555a | -17.31091 | -41.83535 | 2026-10-01 03:40:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9427bfd4-3f38-33f6-b533-d847786f3c52 | -20.10995 | -44.25881 | 2026-10-01 03:40:00 | NOAA-21 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ec913800-a7c4-3169-8c71-114c8b8bd2fa | -15.50556 | -46.1549 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34645249-596a-37f9-a1dc-15cd3a59c02f | -18.54674 | -40.45496 | 2026-10-01 03:40:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af103106-4933-32f7-9c89-3758d711851a | -15.5064 | -46.15076 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c77c119-bdb5-3630-a888-c2f0ea983dc3 | -18.27547 | -42.18537 | 2026-10-01 03:40:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5264686d-d5eb-32de-a20b-c9425140cb55 | -20.18627 | -47.40838 | 2026-10-01 03:40:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 19.0 |
| baf582fe-5eab-33e0-8dfd-06ac3452cf8e | -16.18276 | -42.88116 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73728f06-a045-3458-9e34-f2f50fd08905 | -16.42533 | -47.19147 | 2026-10-01 03:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0c31f56b-5caf-3a32-a91c-2d3dcffd00ce | -20.11524 | -44.39845 | 2026-10-01 03:40:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f35d85d2-fd1b-300c-ac4a-6d2ae07e958a | -15.85371 | -41.7092 | 2026-10-01 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 349707ca-84d0-3e06-95b3-9e348d72cd6f | -20.90262 | -47.41675 | 2026-10-01 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3173e0ad-5a5b-3b65-8194-ae067b7d7e65 | -21.18042 | -47.01655 | 2026-10-01 03:40:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d93c8388-11c3-3f32-b3e0-1c0ffca75fd1 | -16.18189 | -42.88564 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5aabc9f-d7a4-3a57-8917-1be2a489010a | -18.06614 | -44.52131 | 2026-10-01 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 72a9a104-b2c6-392e-9463-16121c64ca39 | -16.17974 | -42.88137 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 803cae0b-c24b-3537-a2e2-1162671b0fc7 | -15.95447 | -45.97371 | 2026-10-01 03:40:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adbe059a-4d5a-3edd-9459-87377920491b | -19.23538 | -42.94227 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 87bb0189-256e-3f3f-82ff-ac55b0b8b28c | -22.14515 | -46.67725 | 2026-10-01 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |


[Clique aqui para ver as próximas entradas](README26.md)
