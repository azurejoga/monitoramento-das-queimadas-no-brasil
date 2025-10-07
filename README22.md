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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 620b29a2-1694-3b4c-b829-f012ada3e1e0 | -11.81194 | -45.11189 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 951705b8-712e-3ab7-9bc9-09bccc238a05 | -7.52573 | -49.90669 | 2025-10-07 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 06a35baa-edb0-3139-aaac-7fc714a35534 | -7.2503 | -44.11881 | 2025-10-07 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e73178c-f463-31ee-8b56-d56edd41a0f0 | -11.7365 | -45.3618 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 377694ef-aacd-3bb3-b3c5-516cd54ce09a | -6.67781 | -42.77665 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1cf8cbaa-fb48-3f9d-bc11-c222f2944d04 | -10.25999 | -44.37071 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27b11d85-8d9d-3aa4-816e-6c98a1671fe6 | -12.23472 | -43.77676 | 2025-10-07 04:08:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cab30d6a-4562-3088-a3ac-2b17aeca9046 | -6.58771 | -44.62528 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed760596-248c-32d5-9881-dcd9cbf01e05 | -8.58163 | -44.3366 | 2025-10-07 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 040d98b2-6967-38f2-8aeb-475a08c98a02 | -6.72384 | -42.82807 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b9a0bc5d-6d71-354a-a365-6a3f0c33cd3c | -11.26859 | -48.84373 | 2025-10-07 04:08:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8104011a-13d6-399f-8e53-9ab2a5c9b1a0 | -8.48429 | -46.28068 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c02b5102-09e8-361d-adb6-7ed95ed50da4 | -7.61134 | -45.48036 | 2025-10-07 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59fcae17-a180-3315-a1eb-e4da995fd9c0 | -7.25376 | -44.11943 | 2025-10-07 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff21392e-b5d3-3045-9c19-765222738652 | -10.23293 | -48.19294 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a5015b1-7744-32bb-b51d-eff43cddc727 | -8.52481 | -46.27289 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6107fa44-6e2a-341b-ae04-13bdfa0603ba | -7.68639 | -42.4065 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 552beecc-3f3b-3eb1-95cc-9b0688745c2c | -11.11992 | -47.21786 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45428d2a-7d86-30ad-a4d6-822b9bb0e319 | -5.73953 | -42.53289 | 2025-10-07 04:08:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a13f34ec-dc9c-3588-9e90-a30a228203b6 | -11.78995 | -45.10049 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5767942a-607f-3ce8-922d-593ae1f8d23d | -7.68641 | -42.57785 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d57a96ea-89e0-3baa-a4b6-25516daa2ed8 | -10.58462 | -51.47365 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1f24b03e-be37-352b-b736-c7f036601c0e | -7.69631 | -42.40806 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3e4fcf73-8b0f-3c8b-bf97-516322605b94 | -8.50292 | -49.13206 | 2025-10-07 04:08:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44c4fbf7-36fd-325e-8571-904a7edab194 | -6.67509 | -41.38898 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a364bc62-068c-391c-a832-ac492352ae54 | -6.0702 | -43.47934 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14e57b36-b730-3a70-906e-852a9c3f1137 | -5.51318 | -41.00775 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b7f2e209-400b-3605-9685-ced435e1ff3b | -9.0353 | -49.76705 | 2025-10-07 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1ba2b4f-d887-3752-b88a-d232dd257480 | -11.95203 | -45.48616 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 152cfd48-ac56-3a0e-be51-7ecc5851a7e3 | -7.26947 | -49.40403 | 2025-10-07 04:08:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd8403fa-2fe1-31e7-bbdc-44b399d18ea5 | -5.98366 | -43.51571 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6966ead9-7821-3d60-907a-29a6cb039a51 | -11.04114 | -50.91727 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9560ccc6-7758-33f6-a098-b17827ff1c13 | -6.45627 | -44.58409 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6482910d-1c89-3ea9-a6fc-a90d9f7cafc0 | -10.26059 | -44.36697 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7db2585c-7b3b-39c3-a422-09e51a0fcb01 | -10.95079 | -51.18449 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 751ed685-536b-369c-bedc-ad0675f264ba | -11.80843 | -45.05236 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29c6b86d-e8cd-30f5-bab4-24f25a838cbd | -6.29784 | -44.05779 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 184381ed-2fed-38e8-8336-1fb5c10060b9 | -7.70237 | -42.39119 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c992efc4-6b79-36e1-baac-3b108899788b | -10.92178 | -47.06343 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3a6a0246-8dec-341e-bd96-f78a339f7d37 | -10.44897 | -50.35226 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 63c96b74-6a01-3a99-a341-cea1eb24af09 | -7.72881 | -42.39536 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 837038a9-fdaf-351f-92bf-869e819309af | -9.00762 | -49.21667 | 2025-10-07 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bc8a034-f708-3a23-b82c-4a985f2cb3f9 | -10.27242 | -44.38044 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20d29e47-0e41-3d68-8576-3646bc65d6fb | -5.70246 | -44.82671 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4419733a-a84e-390b-a335-01dda682e584 | -11.67538 | -46.34327 | 2025-10-07 04:08:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10065983-73dc-3c03-b025-fbd914cb27af | -7.7255 | -42.39484 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 92d70e75-a9d5-33b7-9aee-bbedb7cdf016 | -8.65859 | -46.28814 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64310c4e-c491-35ee-a1a8-386c3191cbd5 | -12.11835 | -45.13525 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 136f211b-39b1-3ff7-8aa7-9056f4d16f23 | -6.72726 | -42.80677 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b72bebd-cf20-396c-904b-710feea89937 | -8.89464 | -47.65393 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eab64cec-5e71-39ae-8dc6-893519f10b4d | -9.18639 | -47.82937 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d948a12e-af7e-394f-a2f5-59c06296bb05 | -5.2948 | -43.09978 | 2025-10-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e86d81b-979e-3d02-82aa-bdf14ce95afe | -10.73259 | -50.48067 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42fe6c51-4d77-3fd3-bceb-32af931367af | -10.25597 | -44.37392 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4c46d65-cef0-3613-86d2-fb4f80ad5037 | -7.01315 | -42.29157 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99635e9c-7094-39db-b610-e63b519b594b | -8.61999 | -54.96016 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd3abff7-302d-3889-8f81-1e752cfdfa01 | -6.58705 | -44.62933 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9bd3934d-e328-392b-ac26-fbc3617dc2ca | -6.72889 | -42.81795 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7003a332-dab3-3614-b668-352c04945e2e | -11.11027 | -43.39885 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4650bac2-a19d-3f22-b076-38a47da35f41 | -8.38241 | -41.85085 | 2025-10-07 04:08:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6e19fb7a-f3f0-3e1f-85cd-7e66d8bf1eef | -6.70593 | -42.18913 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7befa38a-314e-3a44-a18c-bfc4e234a123 | -8.65702 | -46.29769 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63a83056-7048-3e60-9983-7e2e12793e6a | -8.89051 | -47.6532 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 56e03868-2ae7-3409-8fe5-0fe745e6ea2e | -11.03175 | -50.91253 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d519b72-efac-3aca-abca-7896cb6cc008 | -8.49463 | -46.33612 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8e966181-9b4c-38f1-a19b-0e3d5b632e12 | -11.47626 | -43.49508 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cab373c-8fd1-3de7-ac50-00374e16a852 | -6.72718 | -42.8286 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 424a8c7f-0692-3af6-93c9-63a04f30804b | -9.61705 | -48.6016 | 2025-10-07 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 153c9454-f248-3c26-aefc-29460a8ce4ab | -6.4154 | -43.60612 | 2025-10-07 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f52e44af-825a-3bb7-a7b0-0c180c862428 | -8.52717 | -46.25871 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee76fb7c-18ae-3637-b5f7-205652cc2974 | -6.45064 | -42.79179 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e27deeb0-8b35-38e7-96c0-30f269f0f2a2 | -10.2634 | -44.37126 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bb61601-bd2d-3675-a45c-90e3740f1f29 | -9.51586 | -51.36258 | 2025-10-07 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97a0ff11-7a4f-3bf1-aa5a-c8d46fa1c529 | -11.15784 | -47.95716 | 2025-10-07 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d35da032-a629-3883-8bd8-659bb702ff4a | -8.54401 | -46.25154 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f060b43-4b83-3492-9174-3ce4527aac9c | -9.18436 | -47.84098 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b6e3ddf6-12d6-39e4-80d0-df020e9d5b3d | -5.33711 | -43.38393 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65870753-a9a2-3578-8020-80c08b9a0193 | -5.25496 | -46.57032 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fab148a-76ab-31ee-9113-772947acbf8a | -6.24034 | -43.27501 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f30384ba-967b-3229-a14b-98f8c9384287 | -5.25592 | -43.09755 | 2025-10-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c47d7c69-55eb-36b5-8cea-c173f82b5eba | -7.02613 | -42.79233 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| acbeaf3a-96bf-37bb-8391-f13ba53da934 | -6.24374 | -43.27552 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e21f48a9-4ac0-3478-beb6-9ce296feb604 | -6.06713 | -42.57067 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 10d88dec-629d-33e6-a037-9a00b0275d99 | -6.71709 | -42.8488 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fa6db2b6-076c-31f6-be76-ada5e441e8dd | -11.85255 | -45.05955 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3dcfab-495b-3e7b-b30a-1bde6b9cfa5f | -5.25637 | -46.48488 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb05b5fd-be66-334f-a378-fc4672c09a90 | -7.68529 | -42.41347 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7829ec19-3f0d-3ad2-8eb1-cbee5d40038a | -11.78549 | -45.12788 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37b4bdd6-674c-367c-8c22-c2d676d2407b | -11.67464 | -46.34768 | 2025-10-07 04:08:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba942047-ca46-3bb7-9358-9248aa490e69 | -5.24966 | -46.57687 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dff7daa0-7d02-34db-be25-a53bcb460684 | -7.13643 | -46.97344 | 2025-10-07 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16065e4b-91d5-3691-92ec-bdc68557a4ab | -4.59016 | -47.03561 | 2025-10-07 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd30255f-7604-3085-ab92-507129df2f1e | -6.24743 | -43.88314 | 2025-10-07 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 598b1a8c-e45c-3dc9-b924-8deb0d6f7360 | -12.45632 | -45.53625 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56287b92-4be3-3f34-adea-4c46b3282f93 | -11.78587 | -45.10377 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ba792ed-1a79-3ca1-ad2a-3796a154c03a | -10.41406 | -45.38625 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87442f19-0fea-3c57-b13c-535646d90fb8 | -4.69401 | -48.62494 | 2025-10-07 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95678db4-7f3d-372a-a5e2-83e7039c35ad | -6.25462 | -43.25104 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 120b570d-9ad8-3bac-a706-8362459aa09e | -10.38512 | -45.40686 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f3b931a-a917-3f69-ac99-aad1c3d0340a | -10.40476 | -45.37632 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README23.md)
