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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99a1a440-84b5-399c-90db-09821a402ad4 | -19.2365 | -46.869999 | 2024-10-02 00:29:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b33b8ca8-7fdb-3b70-b0a3-153771e7cf5e | -18.3314 | -43.037998 | 2024-10-02 00:29:01 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 477adc2d-1f4b-344d-81df-7f54f41f229f | -18.3332 | -43.045601 | 2024-10-02 00:29:01 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34273055-3381-36a1-875b-c691e0f66724 | -18.3242 | -43.232498 | 2024-10-02 00:29:02 | METOP-B | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8c9d547-68c4-36e5-97f2-7f4772af8d95 | -18.325899 | -43.240002 | 2024-10-02 00:29:02 | METOP-B | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5126b301-0369-3833-b061-6f071d63a7da | -18.3871 | -44.014301 | 2024-10-02 00:29:03 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b83ce72-8180-346e-a501-355cfbece914 | -18.3757 | -44.009399 | 2024-10-02 00:29:04 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0c3a0797-6a3e-310a-bcb9-a316ee65496c | -18.3773 | -44.016701 | 2024-10-02 00:29:04 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6c66de-0c06-3579-b66a-e434336a6508 | -18.378901 | -44.023998 | 2024-10-02 00:29:04 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cc431403-c362-3e73-86a2-c433e564982f | -18.3561 | -44.014099 | 2024-10-02 00:29:04 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bff73c43-14e8-3d67-a1df-17a49c54b69a | -18.3577 | -44.0214 | 2024-10-02 00:29:04 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5ceb9bc7-ff0b-392a-8022-431b3906506d | -18.344801 | -44.0093 | 2024-10-02 00:29:04 | METOP-B | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f5db391b-1594-3c1a-bd5d-3b57f938e4e6 | -18.346399 | -44.016499 | 2024-10-02 00:29:04 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d344d940-9340-3139-af91-0e180aa87169 | -18.348 | -44.0238 | 2024-10-02 00:29:04 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bab5bbfa-233f-3818-8794-f88a75ae2b72 | -18.056299 | -42.605999 | 2024-10-02 00:29:04 | METOP-B | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8d911a8-5390-33c8-a043-b3927c452be3 | -18.058201 | -42.613899 | 2024-10-02 00:29:04 | METOP-B | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e10b114-f402-3ed0-8ed3-3fa7e96e6be8 | -18.106199 | -42.866699 | 2024-10-02 00:29:04 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c05b756-2705-3ebd-953b-c658992865ec | -18.108 | -42.874401 | 2024-10-02 00:29:04 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3020e66f-f89a-338e-b7b0-440e0a3eabad | -17.865299 | -42.185101 | 2024-10-02 00:29:05 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c568e2b8-c670-36e6-b4e9-26c6f294c71e | -17.867201 | -42.193298 | 2024-10-02 00:29:05 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df9456e5-c101-3af9-be9a-0f2699814bdb | -17.700701 | -42.365398 | 2024-10-02 00:29:08 | METOP-B | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c1f2f388-0f38-33b5-9076-91b67a51ba77 | -17.7026 | -42.373501 | 2024-10-02 00:29:08 | METOP-B | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6a92af0a-6c21-39e5-8315-569d4edca4a3 | -17.886801 | -43.990101 | 2024-10-02 00:29:11 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bae40629-b4b8-3c17-990d-8016ccf406bf | -20.0376 | -55.912498 | 2024-10-02 00:29:13 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 087f5d24-cb4d-3699-b127-2f43bd5cbae8 | -20.042 | -55.9408 | 2024-10-02 00:29:13 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2c28f5a2-1544-3e6a-ad8c-43a593a1cc73 | -20.028 | -55.914101 | 2024-10-02 00:29:13 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e892e61e-06ec-30ec-85ce-faa25e75872a | -20.0324 | -55.942402 | 2024-10-02 00:29:13 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca409d18-0e58-3893-8e35-ada2e9c7d0e5 | -19.9946 | -55.445999 | 2024-10-02 00:29:13 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5fa3fd11-2ef1-3f77-9663-d1530791156b | -19.980801 | -55.421501 | 2024-10-02 00:29:13 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ec250a76-59f9-3dee-8720-d7f43ed301f3 | -19.9849 | -55.447601 | 2024-10-02 00:29:13 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b68ed485-8e26-3ca7-8a7d-33e04f990526 | -19.9753 | -55.449299 | 2024-10-02 00:29:13 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0821fb1f-2222-3746-9eb6-0d64f531cd5e | -19.752001 | -54.492401 | 2024-10-02 00:29:14 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d97387b5-9c92-32b9-95f3-ed5adada485b | -18.087799 | -46.134602 | 2024-10-02 00:29:16 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a36fc049-8083-32f3-b73d-501915775c8f | -18.089399 | -46.141998 | 2024-10-02 00:29:16 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4da5fff0-0d41-3547-9196-0292711b73fb | -17.5541 | -44.997398 | 2024-10-02 00:29:20 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e9852a7a-7a55-3db6-912d-49a72426f7bb | -17.555599 | -45.004501 | 2024-10-02 00:29:20 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ddd52cc9-b0e8-32f3-b7f5-86675022a5ef | -17.531799 | -46.7075 | 2024-10-02 00:29:27 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7ef9e96-49c2-39fd-931d-b23b8a14d2ef | -17.5333 | -46.715 | 2024-10-02 00:29:27 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d7c8cd1-55a7-37f6-8ceb-30082539e505 | -18.257601 | -50.8036 | 2024-10-02 00:29:28 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66b7673b-147e-3dbe-9891-887d34743dfa | -18.247801 | -50.805599 | 2024-10-02 00:29:28 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f004e85-7e5e-3274-9b0c-6e7d9d700649 | -18.250099 | -50.817699 | 2024-10-02 00:29:28 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90996070-1b6b-303f-8298-e64f1528a921 | -18.8885 | -54.464699 | 2024-10-02 00:29:29 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c4d5a935-df79-3f20-aeff-7ead18998f1a | -18.8922 | -54.486401 | 2024-10-02 00:29:29 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bb154f44-5b0a-3811-9e46-1b2fcc2d96e5 | -18.878799 | -54.4664 | 2024-10-02 00:29:29 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 90ca4b03-7377-3af3-b45e-b5f5e5886616 | -18.8825 | -54.488098 | 2024-10-02 00:29:29 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2541fa09-1e80-3b5f-9194-96697d1b1895 | -16.413 | -44.085899 | 2024-10-02 00:29:36 | METOP-B | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f29496b-1288-309e-a90a-d4c0b5c751cd | -15.8234 | -42.250999 | 2024-10-02 00:29:38 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34d23a3c-71d5-3aef-a4b6-45544adfb338 | -16.4333 | -46.995701 | 2024-10-02 00:29:46 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7fad11e-ff04-3a3a-9460-752655f3b671 | -16.1227 | -48.006599 | 2024-10-02 00:29:54 | METOP-B | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e1d2c5d-4b43-37c0-81a2-07c495290dea | -17.868 | -57.673599 | 2024-10-02 00:29:54 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cbb1f4cd-64fb-3e18-9b79-4c5ff454f5a7 | -17.8584 | -57.675201 | 2024-10-02 00:29:55 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 44ec0ea0-6060-3fd4-b803-355b9c368f38 | -17.848801 | -57.6768 | 2024-10-02 00:29:55 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b2f2e82b-777e-3993-bc0b-ead925e6dbc4 | -17.839199 | -57.678398 | 2024-10-02 00:29:55 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 79d83a1c-d2fc-3a36-9e54-abfa2666cb0b | -16.3304 | -50.086899 | 2024-10-02 00:29:58 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9df50d5-d772-3d17-a698-8ca5fb4b3a3c | -16.332399 | -50.097198 | 2024-10-02 00:29:58 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 108f8d3b-9f1f-38e1-9b96-802249de49d9 | -17.2048 | -56.09 | 2024-10-02 00:30:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0cac5f7d-6c17-343d-94ae-78bba8011050 | -17.2092 | -56.116402 | 2024-10-02 00:30:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f3f3bba6-7ca0-344d-b735-5e390bd0df70 | -17.2136 | -56.142899 | 2024-10-02 00:30:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5a19a487-2cae-3022-96d6-58f3cc4c895e | -17.195101 | -56.091702 | 2024-10-02 00:30:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f68af69-1bba-379f-b70d-d0c8a517c4ba | -17.199499 | -56.118099 | 2024-10-02 00:30:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ff6cc29a-fe6d-301a-9c28-1673f6450bbe | -17.203899 | -56.1446 | 2024-10-02 00:30:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bccb5d1c-06e2-33e4-9556-006c982b8cb0 | -17.208401 | -56.1712 | 2024-10-02 00:30:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2fa34019-edb8-3ad5-b9ff-5deee3343a8c | -17.212799 | -56.198002 | 2024-10-02 00:30:01 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3b0b710e-2509-3a47-805d-6a678a08b1b6 | -15.7929 | -48.837399 | 2024-10-02 00:30:02 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d2a0816-b437-3906-8d45-a4e3c50e181f | -17.198 | -56.228199 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7e8be11-a015-359b-aa87-6d9f2a662dc3 | -17.1898 | -56.119801 | 2024-10-02 00:30:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 642fc027-75e4-3058-8109-8b271de01166 | -17.194201 | -56.146301 | 2024-10-02 00:30:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 789eb1f6-af07-3127-a92c-816bd2527a19 | -17.1987 | -56.172901 | 2024-10-02 00:30:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2c9a36dd-a62d-341c-9c9a-4947747a43f7 | -17.180201 | -56.121498 | 2024-10-02 00:30:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7c6ffdc5-dd02-3609-b03b-0765cfba9bb4 | -16.104799 | -50.2854 | 2024-10-02 00:30:02 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 433f29b8-a949-33a1-88c3-e53729915d82 | -16.106899 | -50.295898 | 2024-10-02 00:30:02 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27aa6d7b-8290-3e4b-bae8-4254d50d0471 | -16.0951 | -50.287399 | 2024-10-02 00:30:02 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 40a4b7d6-4510-3630-b6f5-ac1b0621a51d | -16.097099 | -50.297901 | 2024-10-02 00:30:02 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83527ed9-04d6-3c97-818f-a8666400fdd6 | -16.099199 | -50.308399 | 2024-10-02 00:30:02 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 12acc7fb-9450-379d-8c30-198c6dda5164 | -16.101299 | -50.319 | 2024-10-02 00:30:02 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7af300f8-6bca-3193-b370-46e57a2771de | -16.085899 | -50.344101 | 2024-10-02 00:30:02 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f54f9ba-8c44-3e13-9335-e5cae48b779b | -15.3368 | -46.7183 | 2024-10-02 00:30:02 | METOP-B | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 29eaaf5d-62cd-3e2c-acd9-a386b0ebed55 | -17.2031 | -56.1996 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ca7046d-a2f6-3f2c-9868-b0e9a3e894d1 | -17.2076 | -56.226501 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61d1a54d-3c8c-3161-8137-67a97895c9fd | -17.184601 | -56.147999 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f47ebbd0-b7ec-34d7-8926-092f7369cc0a | -17.188999 | -56.174599 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64126333-37db-3273-9669-70b72c3e784e | -17.193501 | -56.201401 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d813c495-870b-3d09-8fb8-71e7de53f226 | -17.1793 | -56.1763 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f06ec6a-0ad5-398e-b668-7b3ae5943509 | -17.1838 | -56.203098 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb905f72-d2ad-3a82-883b-d0b39ced012f | -17.188299 | -56.2299 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39645c8e-fe5f-3b01-9022-15d7af3ed504 | -17.160801 | -56.124802 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 248ea10a-4f01-3943-a173-cebd4af47c3d | -17.1653 | -56.151299 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6640ea0b-8897-3ea0-930a-90a81a7131b2 | -17.1467 | -56.100201 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e310b01-abb6-32ea-9449-6615bc04593f | -17.1511 | -56.126598 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9919e5d0-6c52-3c79-83e9-fad711599ebd | -17.1556 | -56.153099 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2abc92f7-305c-32c0-b47c-584589e5a23a | -17.141399 | -56.128201 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1476618-f4f3-3af6-9c60-c4ac1d10702e | -17.145901 | -56.154701 | 2024-10-02 00:30:02 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 25574e3a-1a57-3747-9ad6-e72dac40b876 | -16.086599 | -50.3992 | 2024-10-02 00:30:03 | METOP-B | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 486f872c-1306-3987-a886-1546b85f6d0f | -16.088699 | -50.409801 | 2024-10-02 00:30:03 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 58acc42c-fac7-3a5f-8fdf-d6dc960d80a2 | -15.6216 | -48.108501 | 2024-10-02 00:30:03 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| af8a887e-5118-34e3-b8b6-dfa6d8c413db | -17.079901 | -56.057999 | 2024-10-02 00:30:03 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b333204-461b-325d-8eec-643edcc27816 | -17.0702 | -56.0597 | 2024-10-02 00:30:03 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77efd358-8996-3328-b42c-f91de1b7354a | -15.3845 | -47.420601 | 2024-10-02 00:30:04 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ddc5f124-f585-3a50-93d9-ac40e9d2bdff | -15.3861 | -47.4282 | 2024-10-02 00:30:04 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fd35dae6-e19e-3ed7-b04f-7fd1d0dbc99e | -15.3649 | -47.424999 | 2024-10-02 00:30:04 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
