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
| 3578ed0a-168d-3939-8320-bd40726d699b | -5.59637 | -45.36119 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65e52214-8d91-3a70-a0f3-1643a4718641 | -7.54163 | -47.30699 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31d0e82f-171f-37b3-bdff-9a6e7ada8edc | -10.66721 | -44.80313 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df7f6fc4-cc95-3e17-916d-221d8a001447 | -10.52693 | -50.00518 | 2025-10-29 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0fcf6ea6-1c2e-3e3a-abde-156b6e8501f5 | -6.62994 | -47.18386 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88549353-798e-3823-8a64-9c686f0db9b5 | -9.88759 | -44.88347 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e692925-240e-3b07-a920-57ed3779017b | -6.51166 | -47.02676 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2057238-5a7e-327a-bc75-c3a9a443f3ed | -5.34644 | -46.8651 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccc59307-d4aa-3a69-92d5-8b0fc500ed92 | -8.26381 | -46.35017 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3afec43a-8735-3a22-9406-f43239e585e4 | -8.55264 | -45.68885 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebc79e62-b1f3-3ea2-9bb5-fdb0c980bf18 | -8.35411 | -48.16953 | 2025-10-29 04:23:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef4d7af9-050a-39e4-84c6-d6af097153d0 | -10.51504 | -47.71884 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce3a79ea-dbf0-3a1b-a7cc-9bb2d60f079c | -9.44307 | -46.90367 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41c41418-8b05-37f8-b0fa-3a09633c7e5a | -9.44942 | -46.88605 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e85f0a3-37b4-3cbf-b26f-f7c8fc225f46 | -6.12887 | -41.84542 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 2c632114-0f08-34ae-b69f-46fae8b1fa32 | -6.66888 | -42.67733 | 2025-10-29 04:23:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b914da18-5e7f-3a38-9b3a-cbac858b7636 | -10.77206 | -44.62529 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c620fb34-7b99-317d-ac1e-9669eea728fb | -7.08151 | -44.94014 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7bee0b1f-9ea3-3544-9152-a56a5b1ea4e5 | -10.92445 | -47.61168 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 136cbded-e2d8-3459-938a-aba5ee6af471 | -6.14793 | -41.84008 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f22682d-41a9-3778-92b3-12667d81214d | -9.01544 | -43.9769 | 2025-10-29 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c86be895-45d4-399e-8f51-4e4cd1712f94 | -7.86419 | -44.24139 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 920c5061-b3ad-3ae6-a0ad-7e97315052aa | -5.48207 | -46.44355 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfceff82-28bf-3c6b-83d0-d1bd30ba794b | -10.56752 | -49.83479 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 08ca7996-f3d5-325e-ac89-367ae49204bb | -10.545 | -45.04887 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecacc180-212a-3aba-8d24-04e5c8e650f9 | -10.59096 | -48.04221 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0735d61-d921-369c-bd7e-d4ca37f199c7 | -10.90368 | -48.37834 | 2025-10-29 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ab972ac-85a0-3d1e-9597-b51c8ed29d55 | -7.61362 | -43.5881 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e276ef3-e62d-30db-8624-4d484b56b556 | -6.43696 | -45.07996 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1d64913-b6fd-3844-9720-c8ef0da0675f | -10.76397 | -47.88921 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44982eea-d0be-3d4f-9aae-c79bca8558aa | -10.52159 | -47.74348 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41cf7396-38b2-3fc1-bf0a-0e1a380dac22 | -10.50688 | -47.72527 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8c1b06a-8b8b-3fa9-ae8b-2967464e72a3 | -10.64369 | -48.09238 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eed82ed-68d7-3235-8c45-6b0615950ea2 | -10.51877 | -47.73912 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aae85a27-05b8-3291-9899-708322f908df | -7.59553 | -43.57044 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 667dd3c9-539c-34f3-8338-fd7db7b09669 | -6.4632 | -43.55876 | 2025-10-29 04:23:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 892f7e7b-733c-3ad6-8966-200cad388b49 | -6.99757 | -42.78862 | 2025-10-29 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2dd2d59d-dfbc-3b00-a345-2c70536892f1 | -8.01961 | -47.38295 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c6dab18-3661-3a24-9663-cd6438e6bd6d | -5.45263 | -44.69587 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5444a7b4-3dd7-3a24-a80c-8d57231e9016 | -6.1188 | -41.70892 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e5301e4a-14a3-3bf6-80eb-e7076a126904 | -5.6476 | -43.28336 | 2025-10-29 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43834e5f-a6eb-3955-9f97-cc3713f6847e | -7.34031 | -42.47741 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d8e9098a-70ba-3cf3-89fb-64c96398e1b1 | -7.12765 | -46.98285 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 330b4272-e02b-3c79-b971-9e0dbd15b718 | -7.34559 | -42.46626 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4e121a05-a3c9-3752-9cc4-2debbadc8771 | -7.91993 | -45.70688 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a37964f0-278d-3cd0-8adb-f81bddf3f86e | -7.79458 | -46.4636 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b35a357-5fb2-36d3-86a6-d5b77ba7089c | -4.96587 | -47.77991 | 2025-10-29 04:23:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e3685ca-303c-307d-a586-00d3d7908eac | -5.3332 | -44.84752 | 2025-10-29 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f85bbb0-ed9a-38ef-a471-12848f4165f5 | -6.18145 | -41.69133 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0e61df66-91d4-3ac1-8e8d-060ba908835f | -6.15158 | -41.816 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c3a45811-6e02-3368-bb27-a0387ff37c20 | -7.60175 | -43.57514 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1484968b-afee-32d4-b5c0-a591da6e3ce1 | -10.76785 | -44.7422 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3960c51e-d45b-3be7-9466-a347fd8a6f9b | -10.63951 | -47.8998 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5737abdc-b337-3ac9-8a04-527b911c8dfb | -9.49782 | -46.99534 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cd27269-9496-3c26-ac04-dc52e93eb689 | -12.31923 | -46.91912 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4683b0c0-3588-3e53-9504-1c2ab4d18a4c | -11.28694 | -47.55131 | 2025-10-29 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecdf2cf3-c7ed-35ec-8628-3a8ea04523b5 | -14.13057 | -44.07128 | 2025-10-29 04:25:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4487ca3-022d-3029-ac95-464aa30095f0 | -13.12822 | -47.75045 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aac598d-7ce6-3aef-9400-0e298c3af7f7 | -13.04774 | -43.82533 | 2025-10-29 04:25:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a33ce58-14d1-3572-9024-b51ddc746f04 | -13.3474 | -46.34807 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42bd9d92-c5eb-399c-8a4d-de7571b5374a | -15.93435 | -44.73565 | 2025-10-29 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d0d9fe1-6a7e-3033-a231-589862e984c5 | -13.30488 | -47.69273 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64e7cf88-19d7-3dfc-8f27-0d0d955d40f1 | -13.60871 | -46.49615 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 693acfc7-6747-3698-828a-3585d3fccf6d | -18.9304 | -45.05367 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 069ec8b0-85aa-350e-8ba3-22ed4c54fcd2 | -13.93709 | -48.44474 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52f7d15f-6248-3cb1-97da-f6834ca94bcf | -12.11351 | -46.57401 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 852b2f57-0761-3692-b2ea-29efe0181ff0 | -11.78674 | -44.16556 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 429f8151-f28e-355b-9f5f-b2450f4ef252 | -13.87453 | -48.48054 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c474d7aa-4828-3cac-89f3-51a8ad3293e9 | -17.13808 | -45.37419 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3964f47b-df01-36e5-b67d-fd38cd52b5f2 | -11.88234 | -44.43063 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 747db1b5-5656-3835-ac47-36a1bd4d44fb | -13.5242 | -47.3362 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08c9c17e-1c8c-35d3-886f-effde3077881 | -13.74466 | -48.396 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3505acee-a83a-3cae-8310-aeb35c8f0b49 | -14.67821 | -46.3614 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90883d79-cb70-3278-bc0e-a47a9b543987 | -15.17287 | -47.20982 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88a2a9ec-caff-3ddf-976c-f5a35db0d252 | -14.83034 | -47.40326 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 219b17b5-d286-312b-b5f0-e1b6dc394e83 | -13.37305 | -47.38862 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3fac882-259e-3e09-b974-ec1e0c0fbb99 | -14.26816 | -47.31959 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cd9c09d-00a8-372d-b6c3-14bd3ad7f509 | -11.01234 | -47.84657 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71047613-06eb-399c-a662-ec82f3874d74 | -13.64261 | -46.51244 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c35cd454-8d4c-3a75-8379-90ee5574c214 | -12.21139 | -47.30827 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 046d25e3-7e30-35a6-8c1e-40a1c5a64ddf | -19.32995 | -43.04541 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b68fd92f-f8dc-3449-97e1-1c796668c378 | -13.58741 | -47.61501 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58d2cf79-9d3e-3f08-a755-9365e86a37cc | -15.3084 | -48.05253 | 2025-10-29 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be39f401-2a62-3e55-ae0b-d5f90622fd27 | -13.62008 | -47.60547 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d29181d-1dab-312c-8620-a9ecf2c4a002 | -12.79288 | -44.01228 | 2025-10-29 04:25:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6479064-1df4-3217-bb45-67630a00bef8 | -18.92804 | -45.04495 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a560b163-42f5-312d-9386-59e7a6c66959 | -13.64845 | -48.45135 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a83d4412-bb3a-308d-94d3-9c38c420b47d | -13.94621 | -48.46601 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1679b29-aa3d-3a38-9835-97ed64d7b0e4 | -14.60887 | -48.43599 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0ceb8b3-f315-3048-99bd-ccc66e32cdc4 | -13.21814 | -47.07145 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4db5e3f7-77b0-3495-91af-dc625b368692 | -13.47804 | -47.45055 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f918dd2a-4a32-3a79-a3cc-fb304d320f6c | -16.11578 | -45.75358 | 2025-10-29 04:25:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14994ae9-d271-323c-bb5d-c26fb15c1533 | -12.85566 | -48.63002 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53f38916-d3f2-3782-a2ad-4e36f52363e9 | -13.33589 | -47.48001 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 708c2e2b-40a8-3cbf-b151-597960e13603 | -15.11917 | -47.92626 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1c9b4b7-6c2e-3b81-b34c-76a58226a0d1 | -14.02331 | -48.73711 | 2025-10-29 04:25:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 462b8092-fbeb-3ccd-abcf-6c4e027a3f87 | -13.22425 | -47.07609 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2868d363-172c-3f62-8b91-316bd33813a5 | -13.3238 | -47.448 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d48dbc3-ff0b-32f1-bf9b-754def2fcabb | -14.31518 | -48.01338 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7fe28ca4-b02c-3788-afa9-0e587465bee1 | -14.68157 | -46.33999 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README44.md)
