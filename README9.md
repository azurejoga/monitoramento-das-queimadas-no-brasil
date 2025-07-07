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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7d2e9e1-4836-3376-86ca-d18322263dd3 | -14.12042 | -51.30669 | 2025-07-07 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e907b2a-4735-3c80-8b13-0e319bf37b8c | -20.62832 | -55.33321 | 2025-07-07 04:38:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ba49f51-65e0-3fe7-ac18-384152bbc9bc | -25.19281 | -49.32927 | 2025-07-07 04:38:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fa8d575b-d8ab-3aec-b0ab-a9df41db60a3 | -23.73666 | -51.82209 | 2025-07-07 04:38:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dec9a9b9-3f1a-3fb6-99ac-48e02f906ab7 | -21.19538 | -44.93898 | 2025-07-07 04:38:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 62432adb-891b-3638-8a4c-4e31d1cedf8d | -26.69032 | -53.52176 | 2025-07-07 04:38:00 | NOAA-21 | SÃO MIGUEL DO OESTE | SANTA CATARINA | Brasil | 4217204 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a32a6252-8f0b-3629-a13c-480b69b4e771 | -23.59265 | -47.43987 | 2025-07-07 04:38:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 158ef173-ab3b-35f5-87e1-370a1b4c9c42 | -21.49248 | -47.27403 | 2025-07-07 04:38:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fd11126-4489-3d4b-b484-77e3774b6462 | -22.78572 | -43.75698 | 2025-07-07 04:38:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b1835c65-cf9e-3463-8d60-24581e120ab0 | -21.54894 | -48.7088 | 2025-07-07 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| dfd926ee-ffca-39d3-8666-b1b6a1195000 | -20.9973 | -51.79147 | 2025-07-07 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 49575ef8-d1c9-365a-9dc4-928a410f5711 | -21.96936 | -57.58516 | 2025-07-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22006270-a262-3fe6-8f64-605b037c3bb2 | -24.74538 | -53.80825 | 2025-07-07 04:38:00 | NOAA-21 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 689ec4e0-dd36-30f6-9cd3-585f80b2ec4e | -22.54107 | -48.81133 | 2025-07-07 04:38:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dc371bc-b146-3e90-9a96-43aa3e181406 | -20.63031 | -55.33117 | 2025-07-07 04:38:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40899f1e-a973-3d74-a5bd-696e41a81d5f | -23.33816 | -46.77367 | 2025-07-07 04:38:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30c0471a-7ca3-38ea-bb16-776031e5f82e | -21.1967 | -44.93648 | 2025-07-07 04:38:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0781ebf4-4acd-392a-b392-1eddba951620 | -22.19522 | -45.88201 | 2025-07-07 04:38:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3baa10f-89a6-391c-9ae6-584bd7cd3714 | -21.26372 | -45.68971 | 2025-07-07 04:38:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4161e619-e7c7-33e3-b9d6-66b170a4b799 | -20.58265 | -55.09695 | 2025-07-07 04:38:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4d1daef3-24c2-3475-8434-eda9ebcbbcd7 | -23.9832 | -48.91983 | 2025-07-07 04:38:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fce4e26-4253-378c-86b6-1ce76ff84d25 | -21.02614 | -53.92474 | 2025-07-07 04:38:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4510cc03-7913-3ea6-b2e4-ed8c94ee3d2a | -23.3404 | -46.77316 | 2025-07-07 04:38:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee2a8eb1-71cf-3dbd-aff1-7bfb4f083405 | -22.54134 | -48.81348 | 2025-07-07 04:38:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00f47d0b-de36-3b08-b84a-87db3a6e81f3 | -22.25024 | -50.03896 | 2025-07-07 04:38:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f1640d33-4022-3524-8829-227cb9c43eec | -23.76743 | -55.19638 | 2025-07-07 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 957403fd-da56-3c8f-bc1d-319d6eadaa55 | -21.55247 | -48.70936 | 2025-07-07 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 904f6013-4a89-300b-bc91-54b3c3fd1883 | -21.97347 | -57.5861 | 2025-07-07 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e4633dc-a1c9-310d-adf5-07eb859c39b4 | -22.67532 | -42.85575 | 2025-07-07 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1ae98460-ac64-3cf3-9529-4f7ff570cd5d | -6.1606 | -48.0507 | 2025-07-07 04:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 3aa97ab5-28de-34b1-86b6-2e1aa0d092e7 | -6.1792 | -48.0494 | 2025-07-07 04:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e9fac107-5a8e-39a8-bc86-9473d324fb1d | -6.1604 | -48.0724 | 2025-07-07 04:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b55f41b0-d2c4-3c04-a935-19bcb5c20deb | -28.58535 | -49.44018 | 2025-07-07 04:40:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 880cfc14-6e5f-3703-b6a9-bdc09346dbbd | -28.7732 | -54.78467 | 2025-07-07 04:40:00 | NOAA-21 | BOSSOROCA | RIO GRANDE DO SUL | Brasil | 4302501 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| eb8fc544-f9a1-3f62-ac34-ae9deb6396f2 | -14.1324 | -51.3017 | 2025-07-07 04:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 04e404a8-888a-3c1e-a962-30e1fa6d180d | -6.1606 | -48.0507 | 2025-07-07 04:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 5c190bc1-9857-339a-8e8e-7ad3a47c7741 | -6.1792 | -48.0494 | 2025-07-07 04:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 7d0b7324-7f8b-3da0-9056-a964be24b681 | -4.81615 | -44.35347 | 2025-07-07 04:57:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95127904-a035-3af0-ab5a-b86a48d085fc | -5.59466 | -45.18432 | 2025-07-07 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6619bbad-b987-3731-b25e-ca0f6bb7d20c | -5.59421 | -45.1875 | 2025-07-07 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 423b93eb-dd6a-35b0-bed5-90436695c5a7 | -2.63427 | -47.30711 | 2025-07-07 04:57:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6a5255b-43bd-336e-a3e0-efeb892f94dd | -4.8296 | -45.19845 | 2025-07-07 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dbeee52-a7be-3f4a-ad15-9665d5a51c99 | -4.82164 | -44.35432 | 2025-07-07 04:57:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c38e71d-035b-3a7b-adc8-917b415aab79 | -2.63861 | -47.30776 | 2025-07-07 04:57:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77491d4d-ca96-379c-9047-33518d2f0903 | -5.6013 | -45.1755 | 2025-07-07 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db73b688-28be-380c-92a4-02e8c9dc70ac | -4.28117 | -48.19098 | 2025-07-07 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7de61b5f-fe77-3d4d-ad91-f46122718454 | 0.69275 | -51.46088 | 2025-07-07 04:57:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 605c74c2-b8c4-388c-a667-a061d16154eb | -5.56819 | -45.21962 | 2025-07-07 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2a7bf7f-341e-3b24-ac46-d30422f15df8 | -2.63944 | -47.30726 | 2025-07-07 04:57:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de6aaa28-d90b-3902-92fc-30bc6c5559d2 | -4.03729 | -48.06579 | 2025-07-07 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03889bda-30da-3dfb-9538-67b11bf3023a | -4.28593 | -48.18777 | 2025-07-07 04:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95c406fb-f9f8-3101-9eb0-b2422c79373f | 0.68939 | -51.4614 | 2025-07-07 04:57:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e473f5dd-0fd8-3583-90b9-9a4bba6d61e6 | -2.58707 | -51.92173 | 2025-07-07 04:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebd3cf75-537c-3fce-a09b-4976166fdf8e | -3.92696 | -43.16774 | 2025-07-07 04:57:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48164b20-1bad-32b8-87e6-d9738a7de16a | -5.14172 | -48.8896 | 2025-07-07 04:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9096e4b-0070-31c2-ad7d-375280c4b0bd | -4.82397 | -45.20073 | 2025-07-07 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bddb33c-04df-3a26-9ecb-c49a11922ac5 | -5.56773 | -45.22282 | 2025-07-07 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b342933-8929-3a80-98f8-e767519c45d9 | -2.83799 | -52.37547 | 2025-07-07 04:57:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a397a58-e379-31fe-9be7-c08cfea9e571 | -5.60176 | -45.17228 | 2025-07-07 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b53f96cf-00d6-345e-a5ed-5fa2a69b7a1d | -5.56294 | -45.21886 | 2025-07-07 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7832bb3-48c9-39c0-b618-f1d9725531af | -3.71139 | -53.7095 | 2025-07-07 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8442f8e5-32f5-3a63-9d6d-0971d0dc2e4c | -5.56864 | -45.21641 | 2025-07-07 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c1b7fc5-339e-3307-881c-04a9b070613b | -4.82915 | -45.20157 | 2025-07-07 04:57:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fe22cb7-a457-353a-a065-16618b387f16 | -3.94007 | -49.1298 | 2025-07-07 04:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d31872fd-77af-3662-86cf-e705840072ea | -4.10943 | -48.21302 | 2025-07-07 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cc10d03-7cf7-3d0c-9634-8b89ac759134 | -7.26782 | -44.65472 | 2025-07-07 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74822afa-4fe5-3584-8079-6a7a8d3ed651 | -6.69943 | -43.14977 | 2025-07-07 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4989ce48-7e91-3ed1-b4fd-ef49a1c00bff | -6.30287 | -45.73299 | 2025-07-07 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b2983cc4-3797-39e7-8795-82e4cd5f4040 | -11.88579 | -44.89384 | 2025-07-07 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ca96b98-4f50-36f6-ae4e-1fbc0cfe7773 | -6.71194 | -47.8021 | 2025-07-07 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4272448a-f393-3eed-a357-f8f7574d3138 | -9.76426 | -53.32407 | 2025-07-07 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7526c421-9a2b-3eee-ad29-5c98b17729a8 | -8.06546 | -43.12034 | 2025-07-07 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 07129e80-2d05-3f11-8672-3dc0e4344104 | -7.27354 | -44.61298 | 2025-07-07 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d6cbf01-bf26-319d-be79-af430987b3dd | -10.64794 | -44.48929 | 2025-07-07 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35c48ae2-fc11-3d3d-82ec-62558aeea0b3 | -9.20116 | -45.33887 | 2025-07-07 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0595d5f-e041-303e-89ca-201644da79bd | -6.17355 | -48.05883 | 2025-07-07 04:59:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 5c7619df-20f3-37f2-9919-8e3f31f3215a | -7.70423 | -44.57181 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0f64cd7-a034-3057-82c3-9ed196ae470b | -10.65594 | -46.37586 | 2025-07-07 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70c9880d-7b58-30b4-81d4-bc07ba521d07 | -6.17419 | -48.0545 | 2025-07-07 04:59:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4a605345-1ede-3d37-9de6-09badfb8012b | -9.3496 | -58.84743 | 2025-07-07 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3bc5690-fb70-3387-bccf-e5ef927a842b | -6.64098 | -43.16999 | 2025-07-07 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 031a056f-f61d-3abc-aee0-23b6fa844116 | -8.05924 | -43.11948 | 2025-07-07 04:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4e4534a3-0497-314c-97a6-99c6179cba7b | -10.58065 | -49.12288 | 2025-07-07 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3640905b-d4b8-3035-a493-abdbe600f42c | -9.57824 | -57.39819 | 2025-07-07 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27cef41d-576c-3ff4-8ac3-68e6ba58c589 | -9.53297 | -58.19432 | 2025-07-07 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cfc42d2-12a6-3f1a-808d-bd62804c739f | -6.68779 | -43.14381 | 2025-07-07 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 215954da-228a-3c33-9450-db914bdd5d2b | -10.63432 | -46.37886 | 2025-07-07 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 014f8e57-40b7-3580-9065-839d2885d2ca | -7.69091 | -44.58524 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d14fba9-358f-36e7-b859-05b6726e800c | -7.68628 | -44.57695 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9724add8-859b-3d1b-be72-b4b12d6b6cf0 | -6.70686 | -47.80576 | 2025-07-07 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 36ac9dfe-cdfd-33f5-b830-e230fd25a0c9 | -7.69142 | -44.58149 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f558c87b-87a7-38ff-a569-c7270bd20353 | -8.14163 | -47.16712 | 2025-07-07 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 186c18ff-d205-3a90-b2a8-d82a65f2ed4b | -7.273 | -44.61697 | 2025-07-07 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b11ba7fc-448b-3580-a480-76e30b09b9c1 | -6.3014 | -45.72948 | 2025-07-07 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a82fa80c-9922-329e-96fc-8997e7a6a702 | -9.75742 | -53.30027 | 2025-07-07 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5db48a4e-7f6f-3b4e-b6bb-e19143d3b4fb | -6.16983 | -48.05395 | 2025-07-07 04:59:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| f6852959-5c01-3d08-8ec7-47c2cb4ad78d | -10.04858 | -59.10626 | 2025-07-07 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcc10cae-ad68-38b4-bb75-637365bedc5f | -7.69808 | -44.57478 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c75e68e6-de0f-3f0e-b3b9-fd0f7b7300a3 | -7.68477 | -44.58817 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8f2c7b5-dc91-383c-854c-5fa3a3a4b62c | -7.69858 | -44.57101 | 2025-07-07 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README10.md)
