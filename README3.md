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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22e6bbad-0783-3ad4-b30c-45a8ae0be2c1 | -11.84965 | -46.64168 | 2026-06-03 03:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba3e8b0c-70bf-37c4-afc5-df84d6b57b37 | -7.04793 | -45.06444 | 2026-06-03 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 877aa6dc-9b3d-3c32-8e5c-5df86d100c50 | -7.04878 | -45.05983 | 2026-06-03 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa184997-be02-382f-9b1b-dd0086fe9abb | -6.30484 | -43.64426 | 2026-06-03 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 298c0b0b-8527-3ed1-bd4a-40f16a84ff35 | -7.94865 | -46.84361 | 2026-06-03 03:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39af395d-9fbd-38c0-a497-0725da939d36 | -11.75462 | -47.08072 | 2026-06-03 03:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ab2ea9b-f30c-3f90-9822-fb2b69b7f8d6 | -11.13182 | -45.1456 | 2026-06-03 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2a74e5b-dcc8-3ca2-84a3-abd668e952c8 | -6.76554 | -45.02062 | 2026-06-03 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 87d5b046-6f29-3470-afaf-b4c2f78e5bf8 | -7.26851 | -46.81171 | 2026-06-03 03:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58a2de10-cb4c-3fa5-8eb4-e4b29f15c396 | -6.98889 | -42.88032 | 2026-06-03 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dde8af5b-8a7f-3ad5-a58d-baad3630aad8 | -11.79463 | -42.6349 | 2026-06-03 03:40:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d3a8ac87-e08a-361f-bf38-21e89862e646 | -6.99152 | -42.8758 | 2026-06-03 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 759d0238-81d1-3ffa-8260-4155a482921c | -10.55442 | -46.6282 | 2026-06-03 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 084ac552-3670-3101-9d95-5dd084cb48d5 | -6.99095 | -42.87909 | 2026-06-03 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4bc34f36-7fe0-3471-9f19-2ec4f031005d | -11.13755 | -45.14667 | 2026-06-03 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0955387a-6c05-3ca4-b10c-5a4c2a5b915f | -13.20203 | -43.35627 | 2026-06-03 03:40:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8e44dd1-4c0b-3c53-b5cd-8de9294d46fa | -10.9794 | -45.09982 | 2026-06-03 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b883295-96b6-3d1c-afcd-efffce6ffb1a | -11.99102 | -43.78184 | 2026-06-03 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a0c41b8-3cf1-394d-9594-bdb88506c5e8 | -11.98966 | -45.15043 | 2026-06-03 03:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a709a9ff-cebf-3f6a-a438-d8b2ec265936 | -11.94753 | -43.40775 | 2026-06-03 03:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 119adde7-3cd7-3aea-8ea8-0fb830805d64 | -8.57374 | -45.99884 | 2026-06-03 03:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 26926cb9-a552-33c2-be99-64c6498fa484 | -7.59617 | -46.46534 | 2026-06-03 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84094de7-d693-3317-a188-b796b3c09bad | -11.94921 | -43.39876 | 2026-06-03 03:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b0f2505-355c-3070-b76b-537f9ee8a934 | -10.54702 | -46.63234 | 2026-06-03 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20cce2c9-6998-3e27-8d0e-a24ba74071ee | -11.94865 | -43.40174 | 2026-06-03 03:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59d1512b-6205-3ea2-8573-4748ec6c4f1f | -11.2572 | -48.35646 | 2026-06-03 03:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53ade583-eea2-371c-a0d6-01d473af5c50 | -18.9054 | -41.94064 | 2026-06-03 03:42:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fa2dabe6-698a-3fa8-9157-e13275853974 | -20.08971 | -40.21414 | 2026-06-03 03:42:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bbbee429-b554-3d97-a094-7f8184bdd411 | -18.90476 | -39.8558 | 2026-06-03 03:42:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dfb8c86a-e62a-3d52-b71b-d9d5f11b7b8f | -16.58191 | -45.88431 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7411156c-a737-37ed-ae2f-a84e111e6989 | -16.57748 | -45.87438 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f20b2fcd-0111-3dde-a4c0-ca1a78deb661 | -18.45229 | -40.34929 | 2026-06-03 03:42:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 70c5b598-39fe-3535-839d-6b8a55f72fac | -17.44045 | -42.6353 | 2026-06-03 03:42:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f26651a2-17c6-3278-8288-b91ca63cd5ca | -16.58269 | -45.88065 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fca96647-f289-3dad-9f96-8cded3feaf80 | -13.95491 | -46.19266 | 2026-06-03 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d37dbbbf-62c9-36e3-9cb1-c0640e637e1f | -16.58215 | -45.87923 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e1951784-3a9b-3d0f-a1b4-05c1575ac44e | -17.44131 | -42.63094 | 2026-06-03 03:42:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 00b71d1e-49a3-3389-9126-c2813c86c674 | -20.07714 | -40.17704 | 2026-06-03 03:42:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6868ff13-7c62-3c4c-a64e-620e61c5379a | -17.441 | -42.62833 | 2026-06-03 03:42:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 08aaa209-9c54-3726-89a1-84ebfe0bb5ba | -16.58346 | -45.87703 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6f0e7ced-87f4-3d47-825d-934dbe7075cd | -17.44533 | -42.62923 | 2026-06-03 03:42:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 1630ddeb-31ce-3e31-9cb8-d16514f85977 | -16.57726 | -45.87948 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 15766847-ec88-3468-8f19-abc5a5a903d2 | -16.57598 | -45.88174 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97a67a10-c7ba-3b22-912e-3bf0f2f569e7 | -17.44018 | -42.6327 | 2026-06-03 03:42:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 03f64043-637a-3d31-acbf-84cfe8a356cf | -16.57673 | -45.87804 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2636b708-6110-3fe1-b486-d685e739e203 | -16.58289 | -45.8756 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 47f6663a-75b0-3f00-a443-69ae27a5c44c | -13.95577 | -46.18847 | 2026-06-03 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aca7a072-3f36-3f86-841c-df3ceb6bfce3 | -16.5814 | -45.8829 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7f146778-8ecb-391c-8e29-4d8766e25090 | -17.44649 | -42.62747 | 2026-06-03 03:42:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96db5560-3307-3150-aa44-958fedbcd6f1 | -17.44216 | -42.62658 | 2026-06-03 03:42:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 960ebde2-98a8-33af-b0bc-9a5642472dfa | -16.57804 | -45.87582 | 2026-06-03 03:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a14ba8ef-e53c-3689-834d-fb11f883fe5e | -20.99343 | -48.90279 | 2026-06-03 03:45:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f500a2f8-903a-3aed-8211-6d71cef25df0 | -22.95855 | -52.70105 | 2026-06-03 03:45:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a93bb204-16be-3aae-9738-540e09cb8a53 | -21.69902 | -48.4139 | 2026-06-03 03:45:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc8376e4-a014-3c09-a605-83fa34763cb1 | -20.54866 | -47.20622 | 2026-06-03 03:45:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b49a5f96-004b-38ec-bd60-f65f436ec859 | -21.6998 | -48.41195 | 2026-06-03 03:45:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f562be17-a06f-34a8-afea-9069abb85ec7 | -21.45694 | -41.11815 | 2026-06-03 03:45:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 039df171-0ea9-3924-947f-bd256f6dd902 | -20.88497 | -48.9838 | 2026-06-03 03:45:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 514a95a3-d525-3734-8fd1-6c0a2322e837 | -20.99828 | -48.90911 | 2026-06-03 03:45:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 36a152d3-2afb-38ec-bf93-22d8694633cc | -21.80893 | -49.11936 | 2026-06-03 03:45:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 00e72460-4d16-368c-bc9a-d32c2dcd73bb | -20.99939 | -48.90428 | 2026-06-03 03:45:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 29dfaa41-6442-37de-9719-f5eb47179d2f | -21.69885 | -48.41605 | 2026-06-03 03:45:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4fafae2-3f8c-30fb-b591-c231c07eb690 | -20.54938 | -47.20454 | 2026-06-03 03:45:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d173255a-c58f-3476-9ff7-4762a8e7b133 | -21.81479 | -49.12115 | 2026-06-03 03:45:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e0832712-645d-3007-9abd-92f090afad5c | -20.88384 | -48.98872 | 2026-06-03 03:45:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2722e684-aa37-3728-99ba-62649db8dc90 | -22.96044 | -52.69385 | 2026-06-03 03:45:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bbd257ac-d30c-334e-b648-ad8bac6ac46a | -21.00044 | -48.89972 | 2026-06-03 03:45:00 | NOAA-20 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| ecdc6934-a722-3be4-92cf-750d6d6fe70a | -21.45781 | -41.11343 | 2026-06-03 03:45:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 35ea679a-801f-3d08-9b2a-49cc942ce76c | -21.0028 | -48.9033 | 2026-06-03 03:50:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 162.3 |
| ca20c18d-26f5-3ad3-b43f-9ec17bc23927 | -21.0034 | -48.8801 | 2026-06-03 03:50:00 | GOES-19 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 75c9b9fb-0b79-33e7-8d0b-cdd964fc2258 | -5.04826 | -43.26598 | 2026-06-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a463d67-d390-334c-95ce-c0e1adba3d1f | -5.72761 | -45.03407 | 2026-06-03 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 82f61fed-365a-3557-8645-8ea349e10c96 | -5.30782 | -43.05654 | 2026-06-03 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5261cbec-9d1a-3b44-a4c6-7be085cc5887 | -5.84248 | -43.49345 | 2026-06-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f80b94c-5381-3c3e-bef8-16750f4a9132 | -6.30249 | -43.6433 | 2026-06-03 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90669f0d-d0b9-3626-bc82-001466117afd | -6.76669 | -45.02076 | 2026-06-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bba730d-fc30-3d49-bffc-6c498a0e5824 | -6.74862 | -47.12534 | 2026-06-03 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b9526ac-ee7a-3068-bf62-83209db8865e | -5.72429 | -45.03355 | 2026-06-03 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 09739ad1-e521-3bab-9cef-bdd5fec7f63c | -6.76724 | -45.01719 | 2026-06-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 406e7765-b46f-30a8-b2d4-d3f3e4245c74 | -5.51208 | -35.6001 | 2026-06-03 04:25:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 88d3543f-3e8d-3e1f-ba7d-4d78834b8aea | -6.76165 | -45.00901 | 2026-06-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2a2ad58-f561-397b-8fa6-eff862edfe8a | -5.72483 | -45.03006 | 2026-06-03 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4d064fb7-1fcc-3add-9c65-62fcdce20928 | -6.39067 | -44.17369 | 2026-06-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ccc217d-4a66-34c2-8b72-49180d529a80 | -5.92744 | -43.48524 | 2026-06-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6833608-fa0a-3de0-8693-9b7a82a019d4 | -6.29319 | -43.63391 | 2026-06-03 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5929cb28-952d-3dc8-956a-c4af74ae90a6 | -5.72374 | -45.03706 | 2026-06-03 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 701a0368-d5ad-35d6-ab31-5e8f2b6d77b7 | -5.84308 | -43.48955 | 2026-06-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc6e6224-3cbd-3ad5-ba58-5f0777b4b856 | -6.28971 | -43.63335 | 2026-06-03 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4b78257-4135-3bf1-938e-b45b74847a07 | -5.83839 | -43.49679 | 2026-06-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27d91782-8edb-3e98-a9c4-7fe87d2a874e | -6.76444 | -45.0131 | 2026-06-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c12d3593-02d3-3aee-8949-51aeea15b4ba | -5.83899 | -43.4929 | 2026-06-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cd86bdc-c3ab-38c4-81e3-74122f5747e4 | -6.98875 | -42.8787 | 2026-06-03 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a6e5078f-fa4d-3ef7-b731-6b4ac840b4bf | -6.51018 | -42.21567 | 2026-06-03 04:25:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9722185-b73e-3f08-982e-3e2ebd8c65d5 | -6.7639 | -45.01667 | 2026-06-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dd8109d-6c33-3fa0-8627-9d0404ec5b2c | -6.9924 | -42.87924 | 2026-06-03 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f799774b-7362-37ad-af55-6251202a804f | -5.72707 | -45.03757 | 2026-06-03 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fe1cb3e2-f7d7-31d3-a476-d1991877d0f7 | -6.29029 | -43.62943 | 2026-06-03 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 669d31b8-e827-3b14-b16e-e67c1936c22f | -5.92803 | -43.48135 | 2026-06-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e4e1472-b3eb-3d0d-b512-0cd512d7e7e7 | -6.77004 | -45.02127 | 2026-06-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fcbef87-5fb2-3910-85ed-8a56fe55c768 | -7.10668 | -43.42138 | 2026-06-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
