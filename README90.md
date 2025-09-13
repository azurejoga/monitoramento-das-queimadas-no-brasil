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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b4eb63b-f9ba-3652-87a7-d502cf2a6f09 | -12.10848 | -47.58385 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 389425fb-b24a-3b45-be1a-b5e4ed49c2d5 | -11.77537 | -64.94035 | 2025-09-13 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aacb76f0-19f9-3541-9861-f65f31a74f19 | -15.17057 | -52.49475 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 061d4d65-0639-3910-9859-c7859c9c3562 | -15.86194 | -51.84967 | 2025-09-13 04:59:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7aebab8-e80c-3caf-bf1e-2ecfda5da9fa | -14.43116 | -47.32749 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a125475f-57c3-33d2-acb4-dd10b0481cda | -13.13345 | -47.12883 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cad59c99-cb11-3326-9547-d6d5f2f22ab5 | -14.21548 | -46.26994 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 857faf39-5ce2-3139-860a-45097f76576a | -14.72292 | -55.64046 | 2025-09-13 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59f61bce-0570-390f-9fc7-ca62492a661c | -14.17782 | -46.25701 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e491ce68-0c21-3a85-bb0a-2bc4f0d305ce | -10.7651 | -50.51694 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9cac149-aaab-3b82-b52c-e6915c2b6131 | -12.83732 | -47.92016 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c87d704-5459-303c-acf5-ddf73da2b7c1 | -10.32355 | -58.73406 | 2025-09-13 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 783fd3e2-44a4-3bbf-898d-bbd3c63ebb9f | -15.21332 | -56.68406 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb91cc3e-19b0-3196-9e0d-704691aa44b5 | -15.7785 | -52.25814 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 78a5bde4-b248-30db-ac2a-a2d2672be807 | -14.2034 | -46.27787 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ebbfded5-228b-3fa2-b20b-44709dda78eb | -11.4327 | -43.55456 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c1b8914-84f4-3b88-bab1-e4330e49fafe | -14.19785 | -46.2775 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb6b1e76-0fba-390e-a7fd-b3787b180f9f | -12.92606 | -54.74491 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a234c1df-6dad-3475-bd6e-9ff2a9cea351 | -11.73467 | -46.60217 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d0f02302-8efd-329d-9df1-eb77e5aab7bd | -10.33262 | -54.32312 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ab15e3d-ada5-312b-aca4-cf278956deb0 | -11.43226 | -45.62086 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 3f257b4f-1c14-30ff-8259-ee3ebf87c97b | -10.76482 | -50.54844 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee576483-d224-3d3b-9741-8f245787aa31 | -10.70144 | -54.44621 | 2025-09-13 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa4d96bc-d81e-31ad-9d49-d215ca5f215d | -11.56963 | -50.5794 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a395c9cb-9f1b-34fe-b62f-4e3d7480c5c8 | -12.56698 | -49.12539 | 2025-09-13 04:59:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5994f3f6-16a7-3cfa-8794-33961e8f0535 | -11.42254 | -45.60772 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0bcca8d5-1a79-379e-a769-2a26e58417aa | -14.42649 | -47.32251 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04f419cc-c282-3962-840c-390f8c1c3246 | -15.11796 | -52.47824 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 554d9e6c-a921-366b-860f-44633231c1da | -9.49279 | -55.97399 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d667cb5-40dd-3141-8042-33c6e998b2cc | -14.69849 | -45.14402 | 2025-09-13 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75a3b2b9-2b96-3233-9782-5bb43b9a01a4 | -14.17866 | -46.24983 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d41cd6c-583f-39e2-8c9c-d62783009dbd | -11.42716 | -45.61631 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| ef0ba0b9-82d5-3d9e-9c23-88cbeebf0beb | -9.26477 | -59.40448 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 840c1b14-6dc8-339c-888d-0953abf5ea03 | -11.37119 | -59.14162 | 2025-09-13 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e069934-fe58-3672-874b-622b18102805 | -9.26797 | -59.42252 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| eafbc68a-87a8-340f-bf70-05a835735efb | -11.16208 | -57.18089 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ca3a281-d2e9-3bbb-8440-4755e6b32dd0 | -10.93253 | -56.20867 | 2025-09-13 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e579a5ee-2dbd-3b9e-aa72-8c610cfe1e31 | -12.08554 | -44.89567 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b71c94ad-1863-3868-b3b7-a73a1550b9bd | -9.28244 | -56.89811 | 2025-09-13 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d19cbf1-741d-311a-b881-f3d578352eea | -9.27883 | -59.3919 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c34572be-4adb-3799-ba77-9c68699c457e | -9.26348 | -59.40177 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 187d7a71-f960-37c9-b8e6-65d22f7bee21 | -14.71773 | -59.68624 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9aafce8-1663-3c5b-b685-94d02cdaf629 | -12.8121 | -47.96577 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 772adc8f-1cf2-353b-aed9-ca594e99d332 | -10.74972 | -50.54096 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deca09d8-b1f1-355b-a1d8-3f06a52394cc | -13.25391 | -57.33389 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00679458-b708-3f24-bd6d-0fbd1b1abcb0 | -9.27332 | -59.40089 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bf40bec-20cf-31a2-bf34-721becebf186 | -14.17697 | -46.26435 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| de5fa11f-59e1-3a18-9dcd-51ca742a905f | -11.18464 | -51.42109 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 92370d8b-e716-33b4-b2b0-bf0c19d99fcc | -10.70531 | -54.44319 | 2025-09-13 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd1a013e-4f6f-39bd-883f-01b7c48a74c5 | -14.20229 | -46.23968 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c2a115a7-e3ce-3e31-b1ec-671188ff548b | -14.2032 | -46.27954 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 57dc40d3-73a0-34b3-93ef-af03bb389139 | -14.21339 | -46.28866 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e2a78a8f-6885-3cb4-8677-c0f518d5006a | -10.33982 | -54.32061 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2174113b-015e-323c-a6c1-c4432c69cfc0 | -11.70932 | -46.54777 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4ec2e8d1-3969-35a5-ad53-a73bb9fa8738 | -14.4359 | -46.40221 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e877004-ab5b-3938-8bb2-ad56735a720c | -15.20671 | -56.68296 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0a8ad69-87b1-3b0e-8bf0-02721889a5e5 | -11.27913 | -51.13588 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e6efa15-1ca7-3bad-92e7-af03d55cf9d4 | -13.27072 | -51.70495 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d3ad5848-1f08-3488-a764-dc4cf8fefc25 | -9.16772 | -60.29827 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc90817e-bce7-33a6-aef3-45b9584c28db | -11.14072 | -50.69759 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| a9d39b22-db3a-34a1-b6cc-8a01958a24de | -9.2572 | -59.41567 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 527e6977-11a0-3875-99b9-d0e9a71d2072 | -10.50573 | -51.54868 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fedc57fe-fa53-3ee9-a70e-561c2afe9e28 | -10.70039 | -48.65987 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 52c765d5-e567-3322-865d-45ea88596707 | -10.51025 | -51.5285 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d206e64-42a9-3d02-a982-d35454339f04 | -15.71191 | -50.58649 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b6660b21-b947-3106-8786-df22b28f1c06 | -9.16645 | -60.30567 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43dbf512-36ea-38f5-8132-11e5531c9741 | -11.85843 | -50.57034 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8239dcfd-aed1-3290-9cdd-fb0ef967a198 | -14.21417 | -46.2817 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3d5d791-3f0a-34e3-b4ef-4a7066cf74b0 | -16.41771 | -49.2379 | 2025-09-13 04:59:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7cc3407-3e69-30d9-a8ad-c301a7eb2b31 | -11.10172 | -51.95598 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 158b8354-5229-387f-9e3d-5e9d0c07521d | -11.11641 | -50.69921 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53b9015e-7917-3e65-b552-11303a423f25 | -14.18791 | -46.26665 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| bbe3b0f9-8889-3e4d-8f09-5dba94479bdc | -15.06826 | -48.01791 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 590999f9-4387-38cf-9950-4455e002d269 | -11.01428 | -51.33961 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cea55974-2b61-3378-b06e-1323d6c8d1d0 | -11.41862 | -50.74343 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8ae568b7-9954-378e-add5-cec1087ba645 | -14.19312 | -46.26965 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9ec7158c-f6ee-3f6c-8350-d2801aba81e6 | -15.0954 | -52.50372 | 2025-09-13 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b69d9937-67d3-3559-b058-9c63f79f869a | -14.19723 | -46.28267 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 764bb7d0-abb8-36ce-840a-b9a0f2fcb294 | -15.76366 | -53.49525 | 2025-09-13 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93cef552-bd50-321c-84a5-e7332a487e6f | -11.15867 | -50.71182 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60c24220-e77a-38c2-802e-71ac73ebffd7 | -16.55334 | -49.22245 | 2025-09-13 04:59:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a155e960-bc20-3950-845c-7b80a9756a08 | -10.76906 | -50.51753 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ced14108-c74c-3932-bded-92f44fba9000 | -12.4491 | -44.74695 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10bca21f-4a5e-3fcb-a2dc-2725f06ea224 | -12.94436 | -48.0011 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 041fecdc-8495-3773-a641-19e591f5ab97 | -11.13286 | -50.69643 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| aa3a8a78-041f-31c1-a445-765f92f70bd8 | -12.92162 | -54.75159 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfda4acd-7998-348e-a969-285ebde2b656 | -15.8751 | -51.84354 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b511ba68-7352-3d70-9473-d1e643549fde | -11.35878 | -43.50428 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cab9f89-e4f0-36cc-8eaa-195abb4c632b | -9.13607 | -60.53158 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b9d9fd3-6b20-3fc6-9246-57edcac2e3a2 | -14.1723 | -46.25627 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2854c1f0-13a0-39d4-89d3-b6340c48dfdb | -12.93552 | -54.75009 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 71c0e2bb-492b-32ea-b4ff-ba645f7d21f9 | -14.20224 | -46.23758 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14487284-3b4a-3741-96f3-f802ae8f2fe1 | -11.5741 | -50.57648 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dfcc24f4-a360-30e8-bd5f-b6329dc315ad | -15.77281 | -52.243 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70a0b6c0-6b9b-3ba9-825f-a85c79c724c2 | -11.08262 | -51.43213 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 85c5544a-5129-3cb7-a388-de8c415a23e2 | -12.12486 | -47.59571 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8aabb179-f3dc-390c-9094-2701dd5795a2 | -10.69632 | -49.17719 | 2025-09-13 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d28fec8f-491f-32dc-9b0c-30793d24a3f4 | -14.18198 | -46.26944 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 1b47697f-292f-3f9d-93a1-7315786fd7f1 | -11.77471 | -64.94379 | 2025-09-13 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 143c50ac-4f63-3575-b330-82b280997d72 | -12.38589 | -62.20753 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README91.md)
