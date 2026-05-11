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
| cbaf22bf-adca-34d1-a72e-21b1eabd7676 | -16.98825 | -46.54289 | 2026-05-11 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a275d938-00d9-3608-b9b6-fb09ae7e01b8 | -20.34886 | -40.95047 | 2026-05-11 03:53:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 53f74b4a-8ab2-32cd-b44e-15e49b4668aa | -16.9905 | -46.54057 | 2026-05-11 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cad04cf-e90c-37c9-9600-d9fc7b7e4e96 | -20.34953 | -40.94656 | 2026-05-11 03:53:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| abfc390a-e1f1-35a5-95b4-fcef42deb65a | -14.13338 | -47.39738 | 2026-05-11 03:53:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb1d423d-c4dc-3d15-9a8d-4c9a98359622 | -14.14408 | -45.42364 | 2026-05-11 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc101bdc-a6ad-35c3-9615-77002ba69cbe | -14.14792 | -45.43041 | 2026-05-11 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 547b9ad0-4a1e-3c4b-aaab-655dda951b08 | -14.15395 | -45.42577 | 2026-05-11 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e3a9428-d2cb-3712-9002-36e68f305aa8 | -17.11283 | -41.93383 | 2026-05-11 03:53:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee309db6-d0f0-35c1-aef5-3a47fec44264 | -14.13968 | -47.39518 | 2026-05-11 03:53:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 330a3da3-abae-3100-9f5b-9ead68c01dda | -14.13412 | -47.39379 | 2026-05-11 03:53:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52d2d7da-d467-3464-bbba-26a5b66cbead | -14.15888 | -45.42684 | 2026-05-11 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f6e1214-4be8-3cb1-9613-8a39f8ac5d3b | -7.26735 | -47.0826 | 2026-05-11 04:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d3f5c0b-ef42-30c3-b316-542d634ba85c | -11.03394 | -46.51977 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| afef9e3a-82f2-3203-8f7d-f83c71e7b1b9 | -11.04446 | -46.52642 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04079225-1ed1-3733-a5c0-ff5cb7b5d8fc | -11.05201 | -46.52769 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 220b8528-2a07-36b4-82f0-b71c6d6c8331 | -11.05579 | -46.52833 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2635bd7-02b5-3c99-af70-a7dec9bbde27 | -11.03855 | -46.51558 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5bb6370-8500-3d09-b17a-360a451b7adc | -11.06039 | -46.52415 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef41c05c-941d-3833-b76d-9ae0b4dab814 | -11.04233 | -46.51616 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e7041500-e910-36c3-aae7-672e09c059fe | -11.84446 | -43.96726 | 2026-05-11 04:10:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b5950bce-9781-3795-a086-8a8809f29c99 | -11.03017 | -46.51911 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f2dbae4-971e-357c-b1ce-fdfa0e0dab0f | -7.2626 | -47.0855 | 2026-05-11 04:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecdf9bcd-5164-35ea-b4d8-7979c6aae1b1 | -10.92765 | -44.16997 | 2026-05-11 04:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b06a40f-1b8d-32ce-bdd2-3cc1597a72ec | -7.26323 | -47.08183 | 2026-05-11 04:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1a02be8-cbbc-3155-9d59-09b31e13c9b4 | -11.04149 | -46.52107 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 049ac3ea-fb6d-3590-be0c-a25420fcc46e | -11.03477 | -46.51498 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e6ad1bd0-07ac-37a4-8b82-c7f075455946 | -11.04823 | -46.52706 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bde3b863-4302-32be-9acc-5db53e2c0ff5 | -11.05121 | -46.53237 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d6e917f-1c76-3b99-beee-8e1abbc7f7d7 | -11.05661 | -46.52353 | 2026-05-11 04:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bee40cd-40b8-3e67-95be-48809d1918f2 | -11.52585 | -43.32969 | 2026-05-11 04:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ae7099b-9e6e-335d-b608-7ea17285a3b9 | -7.26673 | -47.08625 | 2026-05-11 04:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a732e09d-28b8-31df-ab94-6771dda5f0fd | -11.76344 | -43.64626 | 2026-05-11 04:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54e76863-a727-3217-8f9a-4b0b10a3898c | -10.93104 | -44.17054 | 2026-05-11 04:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c883992a-e30f-3cb4-b735-32c0d7ab1709 | -13.29003 | -44.20752 | 2026-05-11 04:12:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7f7fb40-331c-37f3-bc50-3a76cbf9d7e7 | -15.24897 | -43.08878 | 2026-05-11 04:12:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 97427b09-322d-3a8d-967d-8e1d7df72255 | -10.53994 | -56.3317 | 2026-05-11 04:12:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 354fbe54-972b-330e-94a7-d08f7c31afab | -14.00053 | -42.54109 | 2026-05-11 04:12:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3eeba488-5a60-3e56-8d11-7907817d81d0 | -14.14161 | -45.42406 | 2026-05-11 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eae79fc3-5565-3040-bc6f-ba15dfbd5992 | -12.79116 | -46.98613 | 2026-05-11 04:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53efe111-2290-3374-82fd-6674aba6a0f0 | -14.15606 | -45.42265 | 2026-05-11 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb3c98c7-fc82-3690-b556-2ca328546e5e | -18.34389 | -43.30462 | 2026-05-11 04:12:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de9bfd24-d54c-30a5-963a-c7df6ecc8386 | -15.88348 | -48.12401 | 2026-05-11 04:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20a7fb7e-dda0-3afc-a751-bcd35ee010e7 | -12.43701 | -41.81122 | 2026-05-11 04:12:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5eadf06f-aba5-393c-a38a-4c93cd9ac97d | -14.15885 | -45.42714 | 2026-05-11 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f69739e-9ef3-3fb7-b83c-b7e3d6035329 | -13.90854 | -42.84686 | 2026-05-11 04:12:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c933973-463e-30bf-925e-1b467c862d03 | -14.14851 | -45.42529 | 2026-05-11 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a7401f8-3333-3625-a46c-fb0a1cfb6ba3 | -14.94437 | -42.79993 | 2026-05-11 04:12:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5a4cadf-fc33-3675-ac4a-f23d7c2ea5e0 | -12.7958 | -46.98192 | 2026-05-11 04:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd169c54-d890-34f9-8af4-7b92949fbb63 | -10.54843 | -56.32602 | 2026-05-11 04:12:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 906ac8c1-2003-3dc8-a5be-cb6f41fd0afb | -10.5453 | -56.32727 | 2026-05-11 04:12:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ade15de-aa01-39b1-a616-59fb9335ed1a | -14.76718 | -47.1561 | 2026-05-11 04:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc7ead6e-3a06-36e5-ba4f-e51970760c26 | -14.15541 | -45.42653 | 2026-05-11 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e09cd14e-2f48-306c-8f28-455afaef3cbc | -13.41943 | -47.51035 | 2026-05-11 04:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f39c9e6b-c587-3c70-b929-3d4168366323 | -16.10508 | -49.23049 | 2026-05-11 04:12:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec0bdf64-e8fc-3177-8180-c27fb84f4c30 | -14.14785 | -45.42916 | 2026-05-11 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e08edec-7dc9-310d-8c80-bfadde960845 | -16.98938 | -46.53956 | 2026-05-11 04:12:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e243b9a0-da26-364c-9597-8b866c23262b | -14.00385 | -42.54163 | 2026-05-11 04:12:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dba05a6d-524d-3f6a-88ae-17a75a72e433 | -12.83017 | -49.79535 | 2026-05-11 04:12:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ecc07f7-e5cd-3fb2-8e68-70fa40e42e28 | -14.00441 | -42.53806 | 2026-05-11 04:12:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4eb73c31-842d-3668-92e7-d9eb2985978d | -14.14571 | -45.4208 | 2026-05-11 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98f69584-91ca-33d2-8d3d-32c6c206b82c | -10.55234 | -56.32867 | 2026-05-11 04:12:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a35050c0-2ed8-3cf2-840a-716e02cd0c26 | -14.14257 | -41.64046 | 2026-05-11 04:12:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 014963cf-34ef-3167-b7aa-70505ed67b91 | -14.13459 | -47.39358 | 2026-05-11 04:12:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7104d4b0-b6ce-31fb-a870-787294390aff | -18.35388 | -43.30634 | 2026-05-11 04:12:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63318741-209f-3c27-a724-842d8577a6b2 | -14.13838 | -47.39432 | 2026-05-11 04:12:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12f598f7-fa06-3d99-aa7d-34d8ae0f1f03 | -16.10436 | -49.23436 | 2026-05-11 04:12:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d2d7e6f-eadc-3939-a3d8-58e89e47956e | -14.14506 | -45.42468 | 2026-05-11 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45251fb1-0709-3562-a53d-2ef4d44649c4 | -10.547 | -56.33303 | 2026-05-11 04:12:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83685dea-9e12-384d-a8ec-eb79b0f5f4a3 | -18.25002 | -51.26819 | 2026-05-11 04:14:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0341447b-a6ed-394f-be8e-88a79a9b5377 | -20.34591 | -40.94929 | 2026-05-11 04:14:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6081e2b-3f49-386e-a0e2-b6070b1e18f9 | -20.34659 | -40.94443 | 2026-05-11 04:14:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 132fbe8f-e955-33ff-a96f-611ea9c46d1e | -20.3491 | -40.94232 | 2026-05-11 04:14:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 03be2fd6-a595-3f85-ab3a-632716e8a8ce | -20.34846 | -40.94714 | 2026-05-11 04:14:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b21e3a3e-b57e-3b76-9c9e-3e60d6ee8e31 | -20.34781 | -40.95204 | 2026-05-11 04:14:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2994c63f-5490-3e3c-8d99-236dcb1c8197 | -28.14095 | -52.70775 | 2026-05-11 04:17:00 | NOAA-20 | COQUEIROS DO SUL | RIO GRANDE DO SUL | Brasil | 4305850 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| a3ab0e7f-630b-3a43-ad39-2e486c713692 | -28.13605 | -52.71086 | 2026-05-11 04:17:00 | NOAA-20 | COQUEIROS DO SUL | RIO GRANDE DO SUL | Brasil | 4305850 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 53d67429-16a7-3525-84b2-a342b3e5714e | 0.70005 | -51.44326 | 2026-05-11 04:55:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed0db685-c5b7-3ab7-b46e-84c44f3b63b6 | -6.91896 | -56.60197 | 2026-05-11 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| db051f33-e874-318c-a16a-cb4d9f55b8d6 | -2.97282 | -60.10279 | 2026-05-11 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e0a9570-ed3a-34f7-8502-d67effe6bb84 | -14.15519 | -45.42672 | 2026-05-11 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a2df684-91ce-3c85-bc39-da7a4124a9d4 | -11.04347 | -46.52004 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7abb1523-24e1-3226-ad60-d8ca19f7c0d3 | -11.04542 | -46.52632 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6153d4a8-0f59-30eb-8366-d904f0e3bde1 | -14.76792 | -47.15543 | 2026-05-11 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a10fc580-28eb-3903-b2ca-9854cb8ac40c | -11.84635 | -43.96821 | 2026-05-11 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4541967e-6c9d-3fe7-846f-8ecf040ae4d9 | -14.15633 | -45.42842 | 2026-05-11 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea954fc9-71ca-3878-92af-56c1789ab199 | -11.03286 | -46.52145 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d6e88a6-8896-3c7a-bad8-e6effc777426 | -11.06038 | -46.53173 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c34ae1a9-fe4d-3ba1-befa-b645be463a0f | -10.55298 | -56.32905 | 2026-05-11 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72ef0d80-eed7-3cea-9dd5-5349855968a5 | -11.05527 | -46.53095 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cdb1fd6-5a05-3c1d-971c-24d8f3d896a4 | -13.17691 | -52.69387 | 2026-05-11 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c82f8d6a-bf80-3fb1-a4c8-5c14a6e96382 | -11.03592 | -46.51881 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35ab3e3e-bd1f-3f87-9892-ed001b6d655c | -11.03324 | -46.5185 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62b9a6ef-bbe2-35a7-82ce-98d971badc70 | -11.04104 | -46.51961 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0cc6be2-eb86-3d20-8332-e3475581fe41 | -11.056 | -46.52508 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbfaa70f-ff94-39d4-96d0-36c3c078b057 | -11.04138 | -46.51687 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afcfd540-edf4-3714-b66f-a90e997f41de | -11.05564 | -46.52796 | 2026-05-11 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2101cb60-03a4-3181-ba83-5a8c7e15f75b | -10.54963 | -56.32851 | 2026-05-11 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53710089-503d-3948-bdd4-61ec1a3c567e | -11.27864 | -55.31226 | 2026-05-11 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9725d9c-4d65-347d-81d8-9b4774746feb | -14.14868 | -52.89697 | 2026-05-11 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
